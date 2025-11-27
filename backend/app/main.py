from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["appdb"]

app = FastAPI()

class Item(BaseModel):
    name: str
    value: int

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/items")
async def create_item(item: Item):
    doc = item.dict()
    res = await db.items.insert_one(doc)
    return {"inserted_id": str(res.inserted_id)}

@app.get("/items", response_model=List[Item])
async def list_items():
    cursor = db.items.find()
    items = []
    async for doc in cursor:
        items.append(Item(name=doc["name"], value=doc["value"]))
    return items

