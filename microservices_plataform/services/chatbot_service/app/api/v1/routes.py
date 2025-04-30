from fastapi import APIRouter
from app.service.conversations import process_conversation
from pydantic import BaseModel

router = APIRouter()

class Message(BaseModel):
    text: str

@router.post("/")
async def talk(message: Message):
    response = process_conversation(message.text)
    return response
