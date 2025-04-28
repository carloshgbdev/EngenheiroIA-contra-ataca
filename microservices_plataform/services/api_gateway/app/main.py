from fastapi import FastAPI
import httpx

app = FastAPI()

client_service_url = "http://localhost:8001/v1/clients"
analytics_service_url = "http://localhost:8002"
chatbot_service_url = "http://localhost:8003"

@app.get("/clientes")
async def get_clientes():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{client_service_url}/")
    return response.json()

@app.post("/previsao")
async def do_predict(dados: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{analytics_service_url}/predict", json=dados)
    return response.json()

@app.post("/chatbot")
async def chatbot(dados: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{chatbot_service_url}/chatbot", json=dados)
    return response.json()
