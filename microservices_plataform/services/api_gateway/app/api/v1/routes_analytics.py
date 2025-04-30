from fastapi import APIRouter
from app.schema.churn_input import ChurnInput
from app.service.analytics_service import get_churn_prediction

router = APIRouter(prefix="/churn", tags=["Churn Prediction"])

@router.post("/", response_model=dict)
async def make_prediction(data: ChurnInput):
    return await get_churn_prediction(data.dict())