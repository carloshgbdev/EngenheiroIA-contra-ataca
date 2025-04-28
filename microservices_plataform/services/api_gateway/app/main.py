from fastapi import FastAPI
import httpx

app = FastAPI()

client_service_url = "http://client_service:8001/v1/clients"
analytics_service_url = "http://analytics_service:8002/v1/analytics"
chatbot_service_url = "http://chatbot_service:8003/v1/chatbot"

@app.get("/clientes")
async def get_clientes():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{client_service_url}/")
    return response.json()

@app.post("/previsao")
async def do_predict(dados: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{analytics_service_url}/", json=dados)
    return response.json()

@app.post("/chatbot")
async def chatbot(dados: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{chatbot_service_url}/", json=dados)
    return response.json()
