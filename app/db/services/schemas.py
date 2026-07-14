from pydantic import BaseModel, ConfigDict


class ServiceCreate(BaseModel):
    title: str
    duration_min: int
    price: int
    description: str | None


class ServiceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    duration_min: int
    price: int
    description: str | None

class CarCreate(BaseModel):
    brand: str
    model: str
    year: int
    price_per_day: int
    is_available: bool

class CarRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    brand: str
    model: str
    year: int
    price_per_day: int
    is_available: bool