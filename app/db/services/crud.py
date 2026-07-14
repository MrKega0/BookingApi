from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.services.model import Car, Service
from db.services.schemas import CarCreate, ServiceCreate


async def get_all(session: AsyncSession) -> list[Service]:
    result = await session.execute(select(Service))
    return result.scalars().all()


async def create(session: AsyncSession, data: ServiceCreate) -> Service:
    service = Service(**data.model_dump())
    session.add(service)
    await session.commit()
    await session.refresh(service)
    return service

async def get_all_cars(session: AsyncSession) -> list[Car]:
    result = await session.execute(select(Car))
    return result.scalars().all()

async def create_car(session: AsyncSession, data: CarCreate) -> Car:
    car = Car(**data.model_dump())
    session.add(car)
    await session.commit()
    await session.refresh(car)
    return car
