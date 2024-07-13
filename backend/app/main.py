from fastapi import FastAPI, Response

from .routers import nba

app = FastAPI()

app.include_router(nba.router)


@app.get("/")
async def root():
    return Response("Server is running")
