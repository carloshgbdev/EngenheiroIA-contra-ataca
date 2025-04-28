from fastapi import APIRouter
from app.service.client_crud import get_all_clients

router = APIRouter()

@router.get("/", tags=["Clients"])
def list_clients():
    return get_all_clients()