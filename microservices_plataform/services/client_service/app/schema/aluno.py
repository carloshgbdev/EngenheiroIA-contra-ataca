from pydantic import BaseModel
from typing import Optional

class AlunoCreate(BaseModel):
    nome: str
    frequencia_semanal: int
    tipo_plano: int

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    frequencia_semanal: Optional[int] = None
    tipo_plano: Optional[int] = None
    ultimo_checkin_id: Optional[int] = None
    
class AlunoResponse(BaseModel):
    id: int
    nome: str
    frequencia_semanal: int
    ultimo_checkin_id: Optional[int] = None
    tipo_plano: int

    model_config = {
        "from_attributes": True
    }