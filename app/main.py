from fastapi import FastAPI

from app.controller import items
from app.controller import offers

app = FastAPI()

app.include_router(router=items.router)
app.include_router(router=offers.router)


@app.get("/")
async def root():
    return {"message": "hello"}
