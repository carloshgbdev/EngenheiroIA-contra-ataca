from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.model import Aluno

async def create_aluno(db: AsyncSession, nome: str, frequencia_semanal: int, tipo_plano: int):
    aluno = Aluno(nome=nome, frequencia_semanal=frequencia_semanal, tipo_plano=tipo_plano, ultimo_checkin_id=None)
    db.add(aluno)
    await db.commit()
    await db.refresh(aluno)
    return aluno

async def get_alunos(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Aluno).offset(skip).limit(limit))
    alunos = result.scalars().all()
    return alunos

async def get_aluno(db: AsyncSession, aluno_id: int):
    result = await db.execute(select(Aluno).filter(Aluno.id == aluno_id))
    aluno = result.scalar_one_or_none()
    return aluno

async def update_aluno(db: AsyncSession, aluno_id: int, nome: str, frequencia_semanal: int, tipo_plano: int, ultimo_checkin_id: int):
    aluno = await get_aluno(db, aluno_id)
    if aluno:
        if nome != None:
            aluno.nome = nome
        if frequencia_semanal != None:
            aluno.frequencia_semanal = frequencia_semanal 
        if tipo_plano != None:
            aluno.tipo_plano = tipo_plano
        if ultimo_checkin_id != None:
            aluno.ultimo_checkin_id = ultimo_checkin_id
            
        await db.commit()
        await db.refresh(aluno)
    return aluno

async def delete_aluno(db: AsyncSession, aluno_id: int):
    aluno = await get_aluno(db, aluno_id)
    if aluno:
        await db.delete(aluno)
        await db.commit()
    return aluno
