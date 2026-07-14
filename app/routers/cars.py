from fastapi import APIRouter

from db.services.crud import create, get_all
from db.services.schemas import CarCreate, CarRead
from deps import SessionDep

router = APIRouter(prefix="/cars", tags=["cars"])


@router.get("")
async def list_cars(session: SessionDep) -> list[CarRead]:
    return await get_all(session)


@router.post("")
async def create_car(data: CarCreate, session: SessionDep) -> CarRead:
    return await create(session, data)
