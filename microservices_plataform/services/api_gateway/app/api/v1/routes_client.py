from fastapi import APIRouter
import app.service.client_service as crud
from app.schema.aluno import AlunoCreate, AlunoUpdate
from app.schema.response import AlunoResponse, GenericResponse

router = APIRouter(prefix="/cliente", tags=["Clients"])

@router.get("/alunos", response_model=GenericResponse[list[AlunoResponse]])
async def list_alunos():
    return await crud.get_alunos()

@router.get("/alunos/{aluno_id}", response_model=GenericResponse[AlunoResponse])
async def get_aluno(aluno_id: int):
    return await crud.get_aluno(aluno_id)

@router.post("/alunos", response_model=GenericResponse[AlunoResponse])
async def add_aluno(aluno: AlunoCreate):
    return await crud.create_aluno(aluno)

@router.put("/alunos/{aluno_id}", response_model=GenericResponse[AlunoResponse])
async def update_aluno(aluno_id: int, aluno: AlunoUpdate):
    return await crud.update_aluno(aluno_id, aluno)

@router.delete("/alunos/{aluno_id}", response_model=GenericResponse[AlunoResponse])
async def delete_aluno(aluno_id: int):
    return await crud.delete_aluno(aluno_id)