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

class CarUpdate(BaseModel):
    brand: str | None = None 
    model: str | None = None 
    year: int | None = None 
    price_per_day: int | None = None 
    is_available: bool | None = None 