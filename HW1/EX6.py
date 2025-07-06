import aiohttp
import asyncio
import time
from functools import wraps

def time_logger(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"{func.__name__} took {duration:.2f} seconds.")
        return result
    return wrapper

class APIClient:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    @time_logger
    async def fetch_data(self, url):
        async with self.session.get(url) as response:
            data = await response.json()
            print(f"Fetched from {url}: {data['title']}")
            return data

    async def close(self):
        await self.session.close()


async def main():
    client = APIClient()

    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
    ]

    tasks = [client.fetch_data(url) for url in urls]
    await asyncio.gather(*tasks)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
