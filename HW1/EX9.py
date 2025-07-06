import aiohttp
import asyncio
from functools import wraps

def log_operation(func):
    @wraps(func)
    async def wrapper(self, ticker, *args, **kwargs):
        price = await func(self, ticker, *args, **kwargs)
        print(f"[LOG] Fetched price for {ticker}: {price}")
        return price
    return wrapper


class StockChecker:
    url = "https://jsonplaceholder.typicode.com/todos/1"
    def __init__(self):
        self.session = aiohttp.ClientSession()

    @log_operation
    async def get_stock_price(self, ticker):
        async with self.session.get(self.url) as response:
            data = await response.json()
            return data["id"]  # fake price (mock)

    async def track_stock(self, ticker):
        for _ in range(3):  # simulate tracking for 3 cycles
            await self.get_stock_price(ticker)
            await asyncio.sleep(5)

    async def close(self):
        await self.session.close()

async def main():
    checker = StockChecker()
    await asyncio.gather(
        checker.track_stock("AMD"),
        checker.track_stock("LLY")
    )
    await checker.close()

if __name__ == "__main__":
    asyncio.run(main())
