from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.cars.model import Car
from db.cars.schemas import CarCreate, CarUpdate

async def get_all(session: AsyncSession) -> list[Car]:
    result = await session.execute(select(Car))
    return result.scalars().all()

async def create(session: AsyncSession, data: CarCreate) -> Car:
    car = Car(**data.model_dump())
    session.add(car)
    await session.commit()
    await session.refresh(car)
    return car

async def get_by_id(session: AsyncSession, car_id: int) -> Car | None:
    stmt = select(Car).where(Car.id == car_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()

async def update(session: AsyncSession, car_id: int, data: CarUpdate) -> Car | None:
    car = await get_by_id(session, car_id)
    if not car:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(car, key, value)

    session.add(car)
    await session.commit()
    await session.refresh(car)
    return car

async def delete(session: AsyncSession, car_id: int) -> bool:
    car = await get_by_id(session, car_id)
    if not car:
        return False
    await session.delete(car)
    await session.commit()
    return True
