from fastapi import FastAPI
from app.api.v1.routes import router

app = FastAPI(
    title="Log Service",
    version="1.0.0",
)

app.include_router(router, prefix="/v1/api", tags=["Logs"])
