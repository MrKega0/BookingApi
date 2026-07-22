from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.cars.model import Car
from db.cars.schemas import CarCreate

async def get_all(session: AsyncSession) -> list[Car]:
    result = await session.execute(select(Car))
    return result.scalars().all()

async def create_car(session: AsyncSession, data: CarCreate) -> Car:
    car = Car(**data.model_dump())
    session.add(car)
    await session.commit()
    await session.refresh(car)
    return car