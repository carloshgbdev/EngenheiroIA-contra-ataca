from fastapi import APIRouter
from app.service.fitness_service import get_fitness_response
from app.schema.fitness_query import FitnessQuery

router = APIRouter()

@router.post("/fitness-assistant")
async def fitness_assistant(query: FitnessQuery):
    answer = get_fitness_response(query.question, query.user_profile)
    return {"response": answer}
