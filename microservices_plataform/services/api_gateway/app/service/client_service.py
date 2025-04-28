import httpx
from app.core.config import settings

async def get_alunos():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.CLIENT_SERVICE_URL}/alunos")
        response.raise_for_status()
        return response.json()

async def get_aluno(aluno_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.CLIENT_SERVICE_URL}/alunos/{aluno_id}")
        response.raise_for_status()
        return response.json()

async def create_aluno(aluno_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.CLIENT_SERVICE_URL}/alunos", json=aluno_data.dict())
        response.raise_for_status()
        return response.json()
    
async def update_aluno(aluno_id: int, aluno_data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{settings.CLIENT_SERVICE_URL}/alunos/{aluno_id}", json=aluno_data.dict())
        response.raise_for_status()
        return response.json()
    
async def delete_aluno(aluno_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{settings.CLIENT_SERVICE_URL}/alunos/{aluno_id}")
        response.raise_for_status()
        return response.json()
