import httpx
from app.core.config import settings

async def get_churn_prediction(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.ANALYTICS_SERVICE_URL}/churn", json=data)
        response.raise_for_status()
        return response.json()