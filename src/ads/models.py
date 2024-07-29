from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped

from src.database import Base


class Ad(Base):
    title: Mapped[str] = Column(String(), nullable=False)
    author: Mapped[str] = Column(String(), nullable=False)
    views: Mapped[int] = Column(Integer, nullable=False)
    index: Mapped[int] = Column(Integer, nullable=False)
