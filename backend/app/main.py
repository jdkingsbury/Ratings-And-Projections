from fastapi import FastAPI, Response

from .api import nba

app = FastAPI()

app.include_router(nba.router)


@app.get("/")
async def root():
    return Response("Server is running")
