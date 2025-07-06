import asyncio
import time
from functools import wraps
import aiofiles

def time_logger(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"{func.__name__} took {duration:.2f} seconds")
        return result
    return wrapper

class FileProcessor:
    def __init__(self, input_file, output_file, keyword):
        self.input_file = input_file
        self.output_file = output_file
        self.keyword = keyword

    @time_logger
    async def process_file(self):
        async with aiofiles.open(self.input_file, mode='r') as infile, \
                   aiofiles.open(self.output_file, mode='w') as outfile:
            async for line in infile:
                if self.keyword in line:
                    await outfile.write(line)

@time_logger
async def process_multiple_files():
    processors = [
        FileProcessor("download_files/animals.txt", "animals_out.txt", "Dogs"),
        FileProcessor("download_files/cakes.txt", "cakes_out.txt", "cream"),
        FileProcessor("download_files/vehicles.txt", "vehicles_out.txt", "cars")
    ]

    tasks = [processor.process_file() for processor in processors]
    await asyncio.gather(*tasks)

# === Run the program ===
if __name__ == "__main__":
    asyncio.run(process_multiple_files())
