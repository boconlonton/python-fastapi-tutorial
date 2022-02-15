"""Contains Offer-related models"""
from typing import Optional
from typing import List

from pydantic import BaseModel

from app.models.items import Item


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]
