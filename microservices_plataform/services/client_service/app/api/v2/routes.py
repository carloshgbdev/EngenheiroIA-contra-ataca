from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import db
from app.service import aluno_crud as service
from app.schema.aluno import AlunoCreate, AlunoUpdate
from app.schema.response import AlunoResponse, GenericResponse
from app.service.publisher import publish_log_event

router = APIRouter()

@router.post("/alunos", response_model=GenericResponse[AlunoResponse], status_code=201)
async def create_aluno(aluno: AlunoCreate, db: AsyncSession = Depends(db.get_db)):
    try:
        create_response = await service.create_aluno(db=db, nome=aluno.nome, frequencia_semanal=aluno.frequencia_semanal, tipo_plano=aluno.tipo_plano)
        
        await publish_log_event(
            action="Criação de Aluno",
            user_id= None,
            details=f"Aluno {create_response.nome} criado com ID {create_response.id}."
        )
        
        success_response = GenericResponse[AlunoResponse](
            success=True,
            status_code=201,
            message="Aluno criado com sucesso.",
            data=create_response
        )
        
        return success_response
    except Exception as e:
        await publish_log_event(
            action="Criação de Aluno",
            user_id= None,
            details=f"Houve uma tentativa não sucedida de criar um aluno."
        )
        
        error_response = GenericResponse(
            success=False,
            status_code=500,
            message="Erro ao criar aluno.",
            data=None
        )
    
        return error_response

@router.get("/alunos", response_model=GenericResponse[list[AlunoResponse]], status_code=200)
async def read_alunos(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(db.get_db)):
    try:
        alunos = await service.get_alunos(db=db, skip=skip, limit=limit)
        
        await publish_log_event(
            action="GET de Alunos",
            user_id= None,
            details=f"Listagem de alunos realizada com sucesso."
        )
        
        success_response = GenericResponse(
            success=True,
            status_code=200,
            message="Alunos listados com sucesso.",
            data=alunos
        )
        
        return success_response
    except Exception as e:
        await publish_log_event(
            action="GET de Alunos",
            user_id= None,
            details=f"Houve uma tentativa não sucedida de listar alunos."
        )
        
        error_response = GenericResponse(
            success=False,
            status_code=500,
            message="Erro ao listar alunos.",
            data=None
        )
    
        return error_response

@router.get("/alunos/{aluno_id}", response_model=GenericResponse[AlunoResponse], status_code=200)
async def read_aluno(aluno_id: int, db: AsyncSession = Depends(db.get_db)):
    try:
        aluno = await service.get_aluno(db=db, aluno_id=aluno_id)
        
        if aluno is None:
            await publish_log_event(
                action="GET de Aluno",
                user_id= None,
                details=f"Aluno não encontrado com ID {aluno_id}."
            )
            
            return GenericResponse(
                success=False,
                status_code=404,
                message="Aluno não encontrado.",
                data=None
            )
        
        await publish_log_event(
            action="GET de Aluno",
            user_id= None,
            details=f"Aluno {aluno.nome} encontrado com ID {aluno.id}."
        )
        
        success_response = GenericResponse(
            success=True,
            status_code=200,
            message="Aluno encontrado com sucesso.",
            data=aluno
        )
        
        return success_response
    except Exception as e:
        await publish_log_event(
            action="GET de Aluno",
            user_id= None,
            details=f"Houve uma tentativa não sucedida de buscar um aluno."
        )
        
        error_response = GenericResponse(
            success=False,
            status_code=500,
            message="Erro ao buscar aluno.",
            data=None
        )
    
        return error_response

@router.put("/alunos/{aluno_id}", response_model=GenericResponse[AlunoResponse], status_code=200)
async def update_aluno(aluno_id: int, aluno: AlunoUpdate, db: AsyncSession = Depends(db.get_db)):
    try:
        update_response = await service.update_aluno(
            db=db,
            aluno_id=aluno_id,
            nome=aluno.nome,
            frequencia_semanal=aluno.frequencia_semanal,
            tipo_plano=aluno.tipo_plano,
            ultimo_checkin_id=aluno.ultimo_checkin_id
        )
        
        await publish_log_event(
            action="Atualização de Aluno",
            user_id= None,
            details=f"Aluno com ID {update_response.id} foi atualizado."
        )
        
        success_response = GenericResponse(
            success=True,
            status_code=200,
            message="Aluno atualizado com sucesso.",
            data=update_response
        )
        
        return success_response
    except Exception as e:
        await publish_log_event(
            action="Atualização de Aluno",
            user_id= None,
            details=f"Houve uma tentativa não sucedida de atualizar o aluno de ID {aluno_id}."
        )
        
        error_response = GenericResponse(
            success=False,
            status_code=500,
            message="Erro ao atualizar aluno.",
            data=None
        )
    
        return error_response

@router.delete("/alunos/{aluno_id}", response_model=GenericResponse[AlunoResponse], status_code=200)
async def delete_aluno(aluno_id: int, db: AsyncSession = Depends(db.get_db)):
    try:
        delete_response = await service.delete_aluno(db=db, aluno_id=aluno_id)
        
        if delete_response is None:
            await publish_log_event(
                action="Remoção de Aluno",
                user_id= None,
                details=f"Aluno não encontrado com ID {aluno_id}."
            )
            
            return GenericResponse(
                success=False,
                status_code=404,
                message="Aluno não encontrado.",
                data=None
            )
        
        await publish_log_event(
            action="Remoção de Aluno",
            user_id= None,
            details=f"Aluno com ID {delete_response.id} foi deletado."
        )
        
        success_response = GenericResponse(
            success=True,
            status_code=200,
            message="Aluno deletado com sucesso.",
            data=None
        )
        
        return success_response
    except Exception as e:
        await publish_log_event(
            action="Remoção de Aluno",
            user_id= None,
            details=f"Houve uma tentativa não sucedida de deletar o aluno de ID {aluno_id}."
        )
        
        error_response = GenericResponse(
            success=False,
            status_code=500,
            message="Erro ao deletar aluno.",
            data=None
        )
    
        return error_response