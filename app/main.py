from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import logger, setup_logging
from app.core.config import settings
from app.api.v1.api import api_router


setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application started")

    yield

    logger.info("Application stopped")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "message": f"{settings.APP_NAME} is running",
        "version": settings.APP_VERSION,
    }