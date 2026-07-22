from fastapi import APIRouter

from db.cars.crud import create_car, get_all
from db.cars.schemas import CarCreate, CarRead
from deps import SessionDep

router = APIRouter(prefix="/cars", tags=["cars"])


@router.get("")
async def list_cars(session: SessionDep) -> list[CarRead]:
    return await get_all(session)


@router.post("")
async def post_create_car(data: CarCreate, session: SessionDep) -> CarRead:
    return await create_car(session, data)