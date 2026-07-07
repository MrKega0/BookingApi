from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.session import create_db_and_tables
from app.routers import services


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(title="Booking API", lifespan=lifespan)
app.include_router(services.router)


@app.get("/")
async def root():
    return {"status": "ok"}
