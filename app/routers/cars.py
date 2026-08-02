from fastapi import APIRouter
from fastapi import HTTPException, Response

from db.cars.crud import create, delete, get_all, get_by_id, update
from db.cars.schemas import CarCreate, CarRead, CarUpdate
from deps import SessionDep

router = APIRouter(prefix="/cars", tags=["cars"])


@router.get("")
async def list_cars(session: SessionDep) -> list[CarRead]:
    return await get_all(session)

@router.post("")
async def post_create_car(data: CarCreate, session: SessionDep) -> CarRead:
    return await create(session, data)

@router.get("/{car_id}")
async def get_car(car_id: int, session: SessionDep) -> CarRead:
    result = await get_by_id(session, car_id)

    if not result:
        raise HTTPException(status_code=404, detail="Car not found")
    return result

@router.patch("/{car_id}")
async def update_car(car_id: int, data: CarUpdate, session: SessionDep) -> CarRead:
    result = await update(session, car_id, data)

    if not result:
        raise HTTPException(status_code=404, detail="Car not found")
    return result

@router.delete("/{car_id}")
async def delete_car(car_id: int, session: SessionDep):
    result = await delete(session, car_id)
    if not result:
        raise HTTPException(status_code=404, detail="Car not found")
    return Response(status_code=204)