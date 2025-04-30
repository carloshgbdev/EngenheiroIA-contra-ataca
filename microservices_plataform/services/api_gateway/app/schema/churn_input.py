from pydantic import BaseModel

class ChurnInput(BaseModel):
    frequencia_semanal: int
    total_checkins: int
    tipo_plano: int