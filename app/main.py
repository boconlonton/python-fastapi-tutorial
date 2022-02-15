from fastapi import FastAPI

from app.controller import items

app = FastAPI()

app.include_router(router=items.router)


@app.get("/")
async def root():
    return {"message": "hello"}
