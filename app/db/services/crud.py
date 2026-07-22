from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.services.model import Service
from db.services.schemas import ServiceCreate, ServiceUpdate


async def get_all(session: AsyncSession) -> list[Service]:
    result = await session.execute(select(Service))
    return result.scalars().all()


async def create(session: AsyncSession, data: ServiceCreate) -> Service:
    service = Service(**data.model_dump())
    session.add(service)
    await session.commit()
    await session.refresh(service)
    return service

async def get_by_id(session: AsyncSession, service_id: int) -> Service | None:
    stmt = select(Service).where(Service.id == service_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()

async def update(session: AsyncSession, service_id: int, data: ServiceUpdate) -> Service | None:
    service = await get_by_id(session, service_id)
    if not service:
        return None
    print(data)
    print(data.model_dump())
    print(data.model_dump(exclude_unset=True))
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(service, key, value)

    session.add(service)
    await session.commit()
    await session.refresh(service)
    return service

async def delete(session: AsyncSession, service_id: int) -> bool:
    service = await get_by_id(session, service_id)
    if not service:
        return False
    await session.delete(service)
    await session.commit()
    return True

