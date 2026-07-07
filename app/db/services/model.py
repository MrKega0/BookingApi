from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Service(Base):
    __tablename__ = "service"

    id: Mapped[int | None] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    title: Mapped[str] = mapped_column(String)
    duration_min: Mapped[int] = mapped_column(Integer)  # длительность услуги в минутах
    price: Mapped[int] = mapped_column(Integer)  # цена в рублях
