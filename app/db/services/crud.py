from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.services.model import Service
from app.db.services.schemas import ServiceCreate


async def get_all(session: AsyncSession) -> list[Service]:
    result = await session.execute(select(Service))
    return result.scalars().all()


async def create(session: AsyncSession, data: ServiceCreate) -> Service:
    service = Service(**data.model_dump())
    session.add(service)
    await session.commit()
    await session.refresh(service)
    return service
