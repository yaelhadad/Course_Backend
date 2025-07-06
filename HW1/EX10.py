import aiohttp
import asyncio
import time
from functools import wraps
import os

def retry(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        for attempt in range(1, 4):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                print(f"[RETRY] Attempt {attempt} failed: {e}")
                await asyncio.sleep(1)
        print(f"[ERROR] Giving up on: {args[0].url}")
        return None
    return wrapper


def time_logger(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"[TIME] Total download time: {duration:.2f} seconds")
        return result
    return wrapper


class ImageDownloader:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.content = None

    @retry
    async def download_image(self, session):
        print(f"[DOWNLOAD] Downloading {self.url}")
        async with session.get(self.url) as response:
            if response.status != 200:
                raise Exception(f"Failed to download: {self.url}")
            self.content = await response.read()
            print(f"[SUCCESS] Downloaded {self.filename}")

    async def save_image(self):
        if self.content:
            os.makedirs("images", exist_ok=True)
            path = os.path.join("images", self.filename)
            with open(path, "wb") as f:
                f.write(self.content)
            print(f"[SAVE] Saved image as {path}")
        else:
            print(f"[ERROR] No content to save for {self.filename}")


@time_logger
async def main():
    urls = [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/200",
        "https://via.placeholder.com/250",
        "https://via.placeholder.com/300",
        "https://via.placeholder.com/350",
    ]

    async with aiohttp.ClientSession() as session:
        downloaders = [
            ImageDownloader(url, f"image{i+1}.jpg") for i, url in enumerate(urls)
        ]


        await asyncio.gather(*(d.download_image(session) for d in downloaders))

        # Save all images
        await asyncio.gather(*(d.save_image() for d in downloaders))

if __name__ == "__main__":
    asyncio.run(main())
