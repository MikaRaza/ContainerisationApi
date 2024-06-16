from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .database import engine, SessionLocal
from .models import Base, Item
from .schemas import ItemCreate, ItemRead
from .crud import get_items, get_item, create_item

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/items/", response_model=List[ItemRead])
async def read_items():
    db = SessionLocal()
    items = get_items(db)
    return items

@app.get("/items/{item_id}", response_model=ItemRead)
async def read_item(item_id: int):
    db = SessionLocal()
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/", response_model=ItemRead)
async def create_item_endpoint(item: ItemCreate):
    db = SessionLocal()
    return create_item(db, item)
