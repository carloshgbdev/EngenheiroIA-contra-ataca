import json
import aio_pika
from typing import Optional
from app.core.rabbitmq import get_rabbitmq_channel

async def publish_log_event(action: str, user_id: Optional[int], details: str):
    log_json = {
        "action": action,
        "user_id": user_id,
        "details": details
    }
    
    channel = await get_rabbitmq_channel()
    message = json.dumps(log_json)
    await channel.default_exchange.publish(
        aio_pika.Message(
            body=message.encode(),
            delivery_mode=2 
        ),
        routing_key="log_events"
    )
