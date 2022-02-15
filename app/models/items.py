from typing import Optional
from typing import Set
from typing import List

from pydantic import BaseModel
from pydantic import Field
from pydantic import HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    """Contains the definition of the item"""
    name: str
    description: Optional[str] = Field(None,
                                       title="The description of the item.",
                                       max_length=300)
    price: float = Field(...,
                         gt=0,
                         description="The price must be greater than zero.")
    tax: Optional[float] = None
    tags: Set[str] = []
    images: Optional[List[Image]] = None

    # Alternative way for creating example in document
    # name: str = Field(..., example="Foo")
    # description: Optional[str] = Field(None, example="A very nice Item")
    # price: float = Field(..., example=35.4)
    # tax: Optional[float] = Field(None, example=3.2)

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }
