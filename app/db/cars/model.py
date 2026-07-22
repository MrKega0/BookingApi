from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base

class Car(Base):
    __tablename__ = "car"

    id: Mapped[int | None] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    brand: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)
    price_per_day: Mapped[int] = mapped_column(Integer)
    is_available: Mapped[bool] = mapped_column(Boolean)