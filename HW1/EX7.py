import aiohttp
import asyncio
from functools import wraps
import time

def logger(func):
    @wraps(func)
    async def wrapper(self, city, *args, **kwargs):
        print(f"[LOG] Fetching weather for: {city}")
        return await func(self, city, *args, **kwargs)
    return wrapper

def retry(func):
    @wraps(func)
    async def wrapper(self, city, *args, **kwargs):
        for attempt in range(1, 4):
            try:
                return await func(self, city, *args, **kwargs)
            except Exception as e:
                print(f"[RETRY] Attempt {attempt} failed: {e}")
                await asyncio.sleep(1)
        raise Exception(f"[ERROR] Failed to fetch weather for {city} after 3 attempts.")
    return wrapper

class WeatherApp:
    url = "https://jsonplaceholder.typicode.com/todos/1"
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.weather_data = {}

    @logger
    @retry
    async def fetch_weather(self, city):
        async with self.session.get(self.url) as response:
            data = await response.json()
            self.weather_data[city] = data

    async def show_weather(self):
        for city in self.weather_data.keys():
            data = self.weather_data.get(city, "No data available")
            print(f"{city}: {data}")

    async def close(self):
        await self.session.close()

async def main():
    app = WeatherApp()
    cities = ["Jerusalem","Tel Aviv", "New York"]
    tasks = [app.fetch_weather(city) for city in cities]
    await asyncio.gather(*tasks)
    await app.show_weather()
    await app.close()

if __name__ == "__main__":
    asyncio.run(main())
