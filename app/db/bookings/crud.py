from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.bookings.model import Booking
from db.bookings.schemas import BookingCreate, BookingUpdate

async def get_all(session: AsyncSession) -> list[Booking]:
    result = await session.execute(select(Booking))
    return result.scalars().all()

async def create(session: AsyncSession, data: BookingCreate) -> Booking:
    booking = Booking(**data.model_dump())
    session.add(booking)
    await session.commit()
    await session.refresh(booking)
    return booking

async def get_by_id(session: AsyncSession, booking_id: int) -> Booking | None:
    stmt = select(Booking).where(Booking.id == booking_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()

async def update(session: AsyncSession, booking_id: int, data: BookingUpdate) -> Booking | None:
    booking = await get_by_id(session, booking_id)
    if not booking:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(booking, key, value)

    session.add(booking)
    await session.commit()
    await session.refresh(booking)
    return booking

async def delete(session: AsyncSession, booking_id: int) -> bool:
    booking = await get_by_id(session, booking_id)
    if not booking:
        return False
    await session.delete(booking)
    await session.commit()
    return True