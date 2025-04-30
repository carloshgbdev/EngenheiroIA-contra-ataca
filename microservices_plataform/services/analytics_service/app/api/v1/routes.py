from fastapi import APIRouter
from app.schema.churn_input import ChurnInput
from app.service.prediction import predict_churn, explain_churn

router = APIRouter()

@router.post("/churn", response_model=dict, tags=["Churn Prediction"])
async def make_prediction(data: ChurnInput):
    prediction = predict_churn(
        frequencia_semanal=data.frequencia_semanal,
        total_checkins=data.total_checkins,
        tipo_plano=data.tipo_plano,
    )
    
    explanation = explain_churn(
        frequencia_semanal=data.frequencia_semanal,
        total_checkins=data.total_checkins,
        tipo_plano=data.tipo_plano,
    )
    
    return {
        "prediction": prediction,
        "explanation": explanation,
    }
