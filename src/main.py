from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from loguru import logger

from src.config import config
from src.ads.router import router as ads_router
from src.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        'redis://localhost', encoding='utf8', decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
    yield

app = FastAPI(
    title=config.APP_NAME,
    version=config.APP_VERSION,
    lifespan=lifespan,
    swagger_ui_parameters={
        'operationsSorter': 'method',
        'defaultModelsExpandDepth': -1
    }
)
app.include_router(ads_router)
app.include_router(users_router)

logger.add('log.txt')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
