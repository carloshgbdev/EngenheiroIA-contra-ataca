import json
import pika
from typing import Optional
from app.core.rabbitmq import get_rabbitmq_channel

def publish_log_event(action: str, user_id: Optional[int], details: str):
    log_json = {
        "action": action,
        "user_id": user_id,
        "details": details
    }
    
    channel = get_rabbitmq_channel()
    message = json.dumps(log_json)
    channel.basic_publish(
        exchange='',
        routing_key='log_events',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)
    )
