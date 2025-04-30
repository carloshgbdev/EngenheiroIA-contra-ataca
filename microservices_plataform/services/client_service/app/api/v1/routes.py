from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import db
from app.service import aluno_crud as service
from app.schema.aluno import AlunoCreate, AlunoUpdate, AlunoResponse

router = APIRouter()

@router.post("/alunos", response_model=AlunoResponse)
async def create_aluno(aluno: AlunoCreate, db: AsyncSession = Depends(db.get_db)):
    return await service.create_aluno(db=db, nome=aluno.nome, frequencia_semanal=aluno.frequencia_semanal, tipo_plano=aluno.tipo_plano)

@router.get("/alunos", response_model=list[AlunoResponse])
async def read_alunos(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(db.get_db)):
    return await service.get_alunos(db=db, skip=skip, limit=limit)

@router.get("/alunos/{aluno_id}", response_model=AlunoResponse)
async def read_aluno(aluno_id: int, db: AsyncSession = Depends(db.get_db)):
    return await service.get_aluno(db=db, aluno_id=aluno_id)

@router.put("/alunos/{aluno_id}", response_model=AlunoResponse)
async def update_aluno(aluno_id: int, aluno: AlunoUpdate, db: AsyncSession = Depends(db.get_db)):
    return await service.update_aluno(db=db, aluno_id=aluno_id, nome=aluno.nome, 
                                      frequencia_semanal=aluno.frequencia_semanal, tipo_plano=aluno.tipo_plano, ultimo_checkin_id=aluno.ultimo_checkin_id)

@router.delete("/alunos/{aluno_id}", response_model=AlunoResponse)
async def delete_aluno(aluno_id: int, db: AsyncSession = Depends(db.get_db)):
    return await service.delete_aluno(db=db, aluno_id=aluno_id)