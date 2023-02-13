import aiohttp
import asyncio


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    async with aiohttp.ClientSession() as session:
        # responses = [await fetcher(session, url) for url in urls]
        responses = await asyncio.gather(*[fetcher(session, url) for url in urls])
        return responses


if __name__ == "__main__":
    asyncio.run(main())
