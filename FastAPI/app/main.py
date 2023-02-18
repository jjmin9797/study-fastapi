from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from service.RobotService import RobotService

# from fastapi.templating import Jinja2Templates


class Item(BaseModel):
    findurl: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world!"}


@app.get("/items/{item_id}")
async def read_item(request: Request, item_id: int):
    return {"item_id": item_id, "REQUEST_HEADER": request["headers"]}


@app.post("/find/robots")
async def findRobots(request: Request, item: Item):
    robotService = RobotService()
    result = await robotService.find(item.findurl)
    result = str(result[0])
    result_l = list(result[2:-1].split("\\n"))
    print(result_l)
    # result = str(result[0])
    return result
