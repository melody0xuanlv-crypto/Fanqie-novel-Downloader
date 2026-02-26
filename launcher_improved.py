import asyncio
import aiohttp

class Downloader:
    def __init__(self, max_workers=5):
        self.max_workers = max_workers
        self.semaphore = asyncio.Semaphore(max_workers)
        self.session = aiohttp.ClientSession()

    async def fetch(self, url):
        async with self.semaphore:
            async with self.session.get(url) as response:
                return await response.text()

    async def download(self, urls):
        tasks = [self.fetch(url) for url in urls]
        return await asyncio.gather(*tasks)

    async def close(self):
        await self.session.close()

async def main(urls):
    downloader = Downloader(max_workers=5)
    try:
        results = await downloader.download(urls)
        # Process results here (e.g., save to file)
    finally:
        await downloader.close()

if __name__ == '__main__':
    urls = ['http://example.com']  # Replace with actual URLs
    asyncio.run(main(urls))