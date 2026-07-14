from fastapi import APIRouter

from db.services.crud import create_car, get_all_cars
from db.services.schemas import CarCreate, CarRead
from deps import SessionDep

router = APIRouter(prefix="/cars", tags=["cars"])


@router.get("")
async def list_cars(session: SessionDep) -> list[CarRead]:
    return await get_all_cars(session)


@router.post("")
async def post_create_car(data: CarCreate, session: SessionDep) -> CarRead:
    return await create_car(session, data)