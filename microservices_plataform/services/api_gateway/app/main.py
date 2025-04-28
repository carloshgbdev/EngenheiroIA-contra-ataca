# from fastapi import FastAPI
# import httpx

# app = FastAPI()

# client_service_url = "http://client_service:8001/v1/clients"
# analytics_service_url = "http://analytics_service:8002/v1/analytics"
# chatbot_service_url = "http://chatbot_service:8003/v1/chatbot"

# @app.get("/clientes")
# async def get_clientes():
#     async with httpx.AsyncClient() as client:
#         response = await client.get(f"{client_service_url}/")
#     return response.json()

# @app.post("/previsao")
# async def do_predict(dados: dict):
#     async with httpx.AsyncClient() as client:
#         response = await client.post(f"{analytics_service_url}/", json=dados)
#     return response.json()

# @app.post("/chatbot")
# async def chatbot(dados: dict):
#     async with httpx.AsyncClient() as client:
#         response = await client.post(f"{chatbot_service_url}/", json=dados)
#     return response.json()

from fastapi import FastAPI
from app.api.v1.routes_client import router as client_router
# from app.api.v1.routes_analytics import router as analytics_router
# from app.api.v1.routes_chatbot import router as chatbot_router

app = FastAPI(
    title="Gateway API",
    version="1.0.0",
    description="Gateway central para comunicação entre microserviços",
    docs_url="/swagger",
    redoc_url="/redoc",
)

app.include_router(client_router)
# app.include_router(analytics_router)
# app.include_router(chatbot_router)
