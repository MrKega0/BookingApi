from fastapi import APIRouter, Request
from fastapi import HTTPException, Response

from db.services.crud import create, delete, get_all, get_by_id, update
from db.services.schemas import ServiceCreate, ServiceRead, ServiceUpdate
from deps import SessionDep
from config import templates

router = APIRouter(tags=["web"])


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"title": "Главная страница"}
    )
