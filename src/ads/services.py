from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.service import BaseCRUD

from src.ads.models import Ad


class AdCRUD(BaseCRUD):
    """Класс описывающий поведение объявлений."""
    __slots__ = ('__id', '__title', '__author', '__views', '__index')

    def __init__(
            self,
            id_: int = None,
            title: str = None,   # Сейчас эти параметры излишни, но если мы
            author: str = None,  # будем добавлять полный CRUD, то пригодятся
            views: str = None,
            index: bool = False
    ):
        self.__id: int = id_
        self.__title: str = title
        self.__author: str = author
        self.__views: str = views
        self.__index: bool = index

    async def get(self, session: AsyncSession) -> Ad | None:
        """Возвращает объект объявления на основе ID объекта CRUD."""
        query = select(Ad).where(Ad.id == self.__id)
        result = await session.execute(query)
        ad = result.scalars().first()
        logger.debug(f'Получен объект ad id{ad.id}')
        return ad
