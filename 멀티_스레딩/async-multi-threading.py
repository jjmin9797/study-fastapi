import aiohttp
import asyncio
import threading
import os


async def fetcher(session, url):
    print(f"{os.getpid()} Process : {threading.get_ident()} URL :{url}")
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 20

    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        # responses = [await fetcher(session, url) for url in urls]
        responses = await asyncio.gather(*[fetcher(session, url) for url in urls])
        return responses


if __name__ == "__main__":
    asyncio.run(main())
