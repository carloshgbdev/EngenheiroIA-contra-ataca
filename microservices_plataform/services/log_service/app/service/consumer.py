import json
import aio_pika
from app.core.rabbitmq import get_rabbitmq_connection
from app.service.log_service import create_log

async def callback(message: aio_pika.IncomingMessage):
    async with message.process():
        data = json.loads(message.body)
        print(f"Foi recebido o evento de LOG: {data}")
        
        await create_log(
            action=data['action'],
            user_id=data['user_id'],
            details=data['details']
        )

async def start_consumer():
    print("Iniciando consumidor...")
    connection = await get_rabbitmq_connection()
    channel = await connection.channel()
    await channel.declare_queue("log_events", durable=True)

    await channel.basic_consume(callback, queue="log_events")
    print("Consumidor pronto.")
