

from fastapi import APIRouter
from fastapi import HTTPException, Response

from db.services.crud import create, delete, get_all, get_by_id, update
from db.services.schemas import ServiceCreate, ServiceRead, ServiceUpdate
from deps import SessionDep

router = APIRouter(prefix="/services", tags=["services"])


@router.get("")
async def list_services(session: SessionDep) -> list[ServiceRead]:
    return await get_all(session)


@router.post("")
async def create_service(data: ServiceCreate, session: SessionDep) -> ServiceRead:
    return await create(session, data)

@router.get("/{service_id}")
async def get_service(service_id: int, session: SessionDep) -> ServiceRead:
    result = await get_by_id(session, service_id)

    if not result:
        raise HTTPException(status_code=404, detail="Service not found")
    return result

@router.patch("/{service_id}")
async def update_service(service_id: int, data: ServiceUpdate, session: SessionDep) -> ServiceRead:
    result = await update(session, service_id, data)

    if not result:
        raise HTTPException(status_code=404, detail="Service not found")
    return result

@router.delete("/{service_id}")
async def delete_service(service_id: int, session: SessionDep):
    result = await delete(session, service_id)
    if not result:
        raise HTTPException(status_code=404, detail="Service not found")
    return Response(status_code=204, detail="Service deleted successfully")
