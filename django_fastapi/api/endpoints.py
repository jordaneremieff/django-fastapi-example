from typing import List

from fastapi import APIRouter

from api import models, schemas


api_router = APIRouter()


@api_router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate):
    item = models.Item.objects.create(**item.dict())

    return item


@api_router.get("/items", response_model=List[schemas.Item])
def read_items():
    items = list(models.Item.objects.all())

    return items
