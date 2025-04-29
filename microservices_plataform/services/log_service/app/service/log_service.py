from app.db.db import db
from app.model.log import LogModel
from datetime import datetime

async def create_log(action: str, user_id: str = None, details: str = None):
    log = LogModel(
        action=action,
        user_id=user_id,
        details=details,
        timestamp=datetime.utcnow()
    )
    result = await db.logs.insert_one(log.dict())
    return str(result.inserted_id)

async def get_logs():
    logs_cursor = db.logs.find()
    logs = []
    async for log in logs_cursor:
        log["_id"] = str(log["_id"])
        logs.append(log)
    return logs
