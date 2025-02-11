from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def root():
    return {"message": "Hello World"}

# path parameters and optional query parameters
# eg. /items/6?q=hello
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "query parameter": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item name": item.name, "item id": item_id}