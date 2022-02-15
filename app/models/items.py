from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel


class Item(BaseModel):
    """Contains the definition of the item"""
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
