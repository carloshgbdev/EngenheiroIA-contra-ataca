from pydantic import BaseModel
from typing import Optional, TypeVar, Generic

T = TypeVar('T')

class GenericResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    status_code: int
    data: Optional[T] = None
    
    model_config = {
        "from_attributes": True
    }
    
class AlunoResponse(BaseModel):
    id: int
    nome: str
    frequencia_semanal: int
    ultimo_checkin_id: Optional[int] = None
    tipo_plano: int

    model_config = {
        "from_attributes": True
    }