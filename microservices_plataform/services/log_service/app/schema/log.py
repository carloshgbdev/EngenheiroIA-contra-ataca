from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogCreate(BaseModel):
    action: str
    user_id: Optional[str]
    details: Optional[str]

class LogResponse(BaseModel):
    id: str
    action: str
    user_id: Optional[str]
    details: Optional[str]
    timestamp: datetime