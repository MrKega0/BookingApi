from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime
from db.bookings.model import BookingStatus

class BookingCreate(BaseModel):
    car_id: int
    customer_name: str
    customer_phone: str
    date_from: datetime
    date_to: datetime
    status: BookingStatus = BookingStatus.active
    
    @field_validator('date_to')
    @classmethod
    def validate_dates(cls, date_to, info):
        date_from = info.data.get('date_from')
        if date_from is not None and date_to is not None:
            if date_from >= date_to:
                raise ValueError('date_from должна быть меньше date_to')
        return date_to

class BookingRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    car_id: int
    customer_name: str
    customer_phone: str
    date_from: datetime
    date_to: datetime
    status: BookingStatus

class BookingUpdate(BaseModel):
    car_id: int | None = None
    customer_name: str | None = None
    customer_phone: str | None = None
    date_from: datetime | None = None
    date_to: datetime | None = None
    status: BookingStatus | None = None

    @field_validator('date_to')
    @classmethod
    def validate_dates(cls, date_to, info):
        date_from = info.data.get('date_from')
        if date_from is not None and date_to is not None:
            if date_from >= date_to:
                raise ValueError('date_from должна быть меньше date_to')
        return date_to