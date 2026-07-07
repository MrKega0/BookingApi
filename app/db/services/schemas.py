from pydantic import BaseModel, ConfigDict


class ServiceCreate(BaseModel):
    title: str
    duration_min: int
    price: int


class ServiceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    duration_min: int
    price: int
