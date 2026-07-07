from fastapi import APIRouter

from db.services.crud import create, get_all
from db.services.schemas import ServiceCreate, ServiceRead
from deps import SessionDep

router = APIRouter(prefix="/services", tags=["services"])


@router.get("")
async def list_services(session: SessionDep) -> list[ServiceRead]:
    return await get_all(session)


@router.post("")
async def create_service(data: ServiceCreate, session: SessionDep) -> ServiceRead:
    return await create(session, data)
