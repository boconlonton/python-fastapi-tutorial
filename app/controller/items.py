"""Contains controllers for the application"""
from typing import Optional
from typing import List

from fastapi import APIRouter
from fastapi import Query
from fastapi import Body
from fastapi import Cookie
from fastapi import Header

from app.models.items import Item
from app.models.items import Image

from app.models.users import User


router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_items(ads_id: Optional[str] = Cookie(None),
                     user_agent: Optional[str] = Header(None),
                     host: Optional[str] = Header(None)):
    return {
        "ads_id": ads_id,
        "User-Agent": user_agent,
        "Host": host
    }


@router.get("/{item_id}")
async def get_item_by_id(item_id: int,
                         q: Optional[str] = Query(None, max_length=3, min_length=1),
                         short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@router.post("/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item


@router.put("/{item_id}")
async def update_item(item_id: int,
                      item: Item,
                      user: User,
                      q: Optional[str] = None,
                      importance: int = Body(...)):
    result = {
        "item_id": item_id,
        "user": user,
        "importance": importance,
        **item.dict()
    }
    if q:
        result.update({"q": q})
    return result


@router.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images
