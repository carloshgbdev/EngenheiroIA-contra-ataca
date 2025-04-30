from fastapi import APIRouter
from app.service.prediction import generate_prediction
from pydantic import BaseModel

router = APIRouter()

class Data(BaseModel):
    parameter: str

@router.post("/")
async def make_prediction(data: Data):
    prediction = generate_prediction(data.dict())
    return prediction
