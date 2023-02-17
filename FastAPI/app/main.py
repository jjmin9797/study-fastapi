from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# from fastapi.templating import Jinja2Templates

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world!"}


@app.get("/items/{item_id}")
async def read_item(request: Request, item_id: int):
    return {"item_id": item_id, "REQUEST_HEADER": request["headers"]}
