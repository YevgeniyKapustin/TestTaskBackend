from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from src.database import Base


class User(Base):
    email: Mapped[str] = Column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = Column(String(length=1024), nullable=False)
