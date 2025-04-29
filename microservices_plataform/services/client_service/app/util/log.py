import httpx
from typing import Optional

async def register_log(action: str, user_id: Optional[int], details: str):
    async with httpx.AsyncClient() as client:
        await client.post("http://log_service:8004/v1/api/logs", json={
            "action": action,
            "user_id": user_id,
            "details": details
        })
