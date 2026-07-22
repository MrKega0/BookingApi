from pydantic import BaseModel, ConfigDict

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