from typing import Annotated

from fastapi import APIRouter, Depends, Query
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from src.ads.schemas import AdScheme
from src.ads.services import AdCRUD
from src.database import get_async_session
from src.schemas import NotFoundScheme
from src.users.models import User
from src.users.services import get_current_user_by_token

router = APIRouter(
    prefix='/api/v1',
    tags=['Объявления'],
)


@router.get(
    '/ads',
    name='Возвращает информацию об объявлении',
    responses={
        HTTP_200_OK: {
            'model': AdScheme,
            'description': 'Объект получен',
        },
        HTTP_404_NOT_FOUND: {
            'model': NotFoundScheme,
            'description': 'Объект не найден',
        }
    }
)
@cache(expire=60)
async def get_command(
        ad_id: Annotated[int | None, Query(title='ID объявления')] = None,
        session: AsyncSession = Depends(get_async_session),
        current_user: User = Depends(get_current_user_by_token)
) -> JSONResponse:
    crud: AdCRUD = AdCRUD(id_=ad_id)
    ad = await crud.get(session)
    if ad:
        return JSONResponse(
            content=AdScheme(
                id=ad.id,
                title=ad.title,
                author=ad.author,
                views=ad.views,
                index=ad.index
            ).dict(),
            status_code=HTTP_200_OK,
        )
    else:
        return JSONResponse(
            content=NotFoundScheme().dict(),
            status_code=HTTP_404_NOT_FOUND,
        )
