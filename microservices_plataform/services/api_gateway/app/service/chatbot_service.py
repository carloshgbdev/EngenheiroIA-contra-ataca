import httpx
from app.core.config import settings

async def send_query_to_chatbot(data: dict):
    async with httpx.AsyncClient(timeout=None) as client:
        response = await client.post(f"{settings.CHATBOT_SERVICE_URL}/fitness-assistant", json=data)
        response.raise_for_status()
        return response.json()