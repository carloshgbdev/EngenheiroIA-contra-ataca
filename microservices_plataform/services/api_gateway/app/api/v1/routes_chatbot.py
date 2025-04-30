from fastapi import APIRouter
from app.schema.fitness_query import FitnessQuery
from app.service.chatbot_service import send_query_to_chatbot

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post("/", response_model=dict)
async def fitness_assistant(query: FitnessQuery):
    return await send_query_to_chatbot(query.dict())