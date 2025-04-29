import aio_pika
from app.core.config import settings

async def get_rabbitmq_connection():
    connection = await aio_pika.connect_robust(
        f"amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}/"
    )
    
    return connection
