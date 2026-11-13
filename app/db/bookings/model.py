from datetime import datetime
from sqlalchemy import Enum as SAEnum
from enum import Enum
from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base

class BookingStatus(str, Enum):
    active = "active"
    cancelled = "cancelled"
    

class Booking(Base):
    __tablename__ = "booking"

    id: Mapped[int | None] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    car_id: Mapped[int] = mapped_column(Integer, ForeignKey("car.id"))
    customer_name: Mapped[str] = mapped_column(String)
    customer_phone: Mapped[str] = mapped_column(String)
    date_from: Mapped[datetime] = mapped_column(DateTime)
    date_to: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[BookingStatus] = mapped_column(SAEnum(BookingStatus), default=BookingStatus.active)