"""Contains controllers for the application"""
from fastapi import APIRouter

from app.models.offers import Offer


router = APIRouter(
    prefix="/offers",
    tags=["offers"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_offer(offer: Offer):
    return offer
