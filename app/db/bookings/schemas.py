from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime

class BookingCreate(BaseModel):
    car_id: int
    customer_name: str
    customer_phone: str
    date_from: str
    date_to: str
    status: str
    
    @field_validator('date_to')
    @classmethod
    def validate_dates(cls, date_to, info):
        if 'date_from' in info.data:
            date_from = datetime.fromisoformat(info.data['date_from'])
            date_to_parsed = datetime.fromisoformat(date_to)
            if date_from >= date_to_parsed:
                raise ValueError('date_from должна быть меньше date_to')
        return date_to

class BookingRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    car_id: int
    customer_name: str
    customer_phone: str
    date_from: str
    date_to: str
    status: str

class BookingUpdate(BaseModel):
    car_id: int | None = None
    customer_name: str | None = None
    customer_phone: str | None = None
    date_from: str | None = None
    date_to: str | None = None
    status: str | None = None
    
    @field_validator('date_to')
    @classmethod
    def validate_dates(cls, date_to, info):
        if date_to and 'date_from' in info.data and info.data['date_from']:
            date_from = datetime.fromisoformat(info.data['date_from'])
            date_to_parsed = datetime.fromisoformat(date_to)
            if date_from >= date_to_parsed:
                raise ValueError('date_from должна быть меньше date_to')
        return date_to