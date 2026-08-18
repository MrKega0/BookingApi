from fastapi import APIRouter
from fastapi import HTTPException, Response

from db.bookings.crud import create, delete, get_all, get_by_id, update
from db.bookings.schemas import BookingCreate, BookingRead, BookingUpdate
from db.cars.crud import get_by_id as get_car_by_id
from deps import SessionDep

router = APIRouter(prefix="/bookings", tags=["bookings"])

@router.get("")
async def list_bookings(session: SessionDep) -> list[BookingRead]:
    return await get_all(session)

@router.post("")
async def post_create_booking(data: BookingCreate, session: SessionDep) -> BookingRead:
    car = await get_car_by_id(session, data.car_id)
    if not car:
        raise HTTPException(status_code=404, detail=f"Car with id={data.car_id} not found")
    return await create(session, data)

@router.get("/{booking_id}")
async def get_booking(booking_id: int, session: SessionDep) -> BookingRead:
    booking = await get_by_id(session, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.put("/{booking_id}")
async def put_update_booking(booking_id: int, data: BookingUpdate, session: SessionDep) -> BookingRead:
    booking = await update(session, booking_id, data)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.delete("/{booking_id}")
async def delete_booking(booking_id: int, session: SessionDep) -> Response:
    success = await delete(session, booking_id)
    if not success:
        raise HTTPException(status_code=404, detail="Booking not found")
    return Response(status_code=204)