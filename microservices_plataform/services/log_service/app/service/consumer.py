import json
import asyncio
from aio_pika import IncomingMessage
from aiormq.exceptions import AMQPConnectionError
from app.core.rabbitmq import get_rabbitmq_channel
from app.service.log_service import create_log
import logging

logger = logging.getLogger("log_consumer")
logger.setLevel(logging.INFO)

async def callback(message: IncomingMessage):
    async with message.process():
        data = json.loads(message.body)
        logger.info(f"recebido evento de LOG: {data}")
        await create_log(
            action=data['action'],
            user_id=data['user_id'],
            details=data['details']
        )

async def start_consumer():
    channel = await get_rabbitmq_channel()
    logger.info("Consumidor de RabbitMQ iniciado com sucesso.")
    queue = await channel.declare_queue('log_events', durable=True)
    await queue.consume(callback)
    await asyncio.Future()

async def run_consumer():
    connected = False
    while not connected:
        try:
            await start_consumer()
            connected = True
        except AMQPConnectionError:
            logger.warning("RabbitMQ indisponível, tentando novamente em 5s...")
            await asyncio.sleep(5)
        except Exception as e:
            logger.exception("Erro inesperado no consumidor; reiniciando em 5s:")
            await asyncio.sleep(5)