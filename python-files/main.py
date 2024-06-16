from fastapi import FastAPI

from .routers import nba_service

app = FastAPI()

app.include_router(nba_service.router)

@app.get("/")
async def root():
    return {"message": "NBA Prediction API home page"}
