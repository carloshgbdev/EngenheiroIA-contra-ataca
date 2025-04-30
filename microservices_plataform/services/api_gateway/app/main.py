from fastapi import FastAPI
from app.api.v1.routes_client import router as client_router
from app.api.v1.routes_analytics import router as analytics_router
from app.api.v1.routes_chatbot import router as chatbot_router

app = FastAPI(
    title="Gateway API",
    version="1.0.0",
    description="Gateway central para comunicação entre microserviços",
    docs_url="/swagger",
    redoc_url="/redoc",
)

app.include_router(client_router)
app.include_router(analytics_router)
app.include_router(chatbot_router)
