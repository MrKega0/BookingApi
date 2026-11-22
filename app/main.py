from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.session import create_db_and_tables
from routers import services, cars, bookings, web


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(title="Booking API", lifespan=lifespan)
app.include_router(cars.router, prefix='/api')
app.include_router(services.router, prefix='/api')
app.include_router(bookings.router, prefix='/api')
app.include_router(web.router)

