from fastapi import APIRouter
from app.service.log_service import create_log, get_logs
from app.schema.log import LogCreate

router = APIRouter()

@router.post("/logs")
async def create_log_entry(log: LogCreate):
    log_id = await create_log(
        action=log.action,
        user_id=log.user_id,
        details=log.details
    )
    return {"log_id": log_id}

@router.get("/logs")
async def list_logs():
    logs = await get_logs()
    return logs
