import aiohttp
import asyncio
from config import get_secret
import aiofiles
import os


async def img_downloader(session, img):
    image_name = img.split("/")[-1]
    try:
        os.mkdir("./images")
    except:
        pass
    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{image_name}", mode="wb") as file:
                image_data = await response.read()
                await file.write(image_data)


async def fetch(session, url):
    headers = {
        "X-Naver-Client-Id": get_secret("NAVER_API_KEY"),
        "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET"),
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]

        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
        ) as session:
            await asyncio.gather(*[img_downloader(session, image) for image in images])


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    KEYWORD = "twice"
    urls = [f"{BASE_URL}?query={KEYWORD}&display=10&start={1+i*20}" for i in range(10)]
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())
