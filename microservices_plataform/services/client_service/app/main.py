from fastapi import FastAPI
from app.api.v1.routes import router as client_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(client_router, prefix="/v1/clients")
