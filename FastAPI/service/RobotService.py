import aiohttp
import asyncio


class RobotService:
    ROBOT_PLUS = "robots.txt"

    def findRobot(self, url):
        if url[-1] != "/":
            url += "/" + self.ROBOT_PLUS
        else:
            url += self.ROBOT_PLUS
        return url

    async def getRobotFile(self, session, url):
        async with session.get(url) as response:
            result = await response.read()
        return result

    async def find(self, url):
        url = self.findRobot(url)
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
        ) as session:
            return await asyncio.gather(self.getRobotFile(session, url))
