import asyncio
class FileDownloader:

    def __init__(self,file_url,file_name):
        self.file_url = file_url
        self.file_name = file_name

    async def download_file(self):
        print(f"Starting download {self.file_name} from {self.file_url}")
        await asyncio.sleep(2)
        print(f"Finished download {self.file_name}from {self.file_url}")

async def main():

    file1=FileDownloader("download_files/animals.txt","animals")
    file2=FileDownloader("download_files/cakess.txt","cakes")
    file3=FileDownloader("download_files/vehicles.txt.txt","vehicles")
    await asyncio.gather(file1.download_file(),file2.download_file(),file3.download_file())

if __name__ == "__main__":
    asyncio.run(main())