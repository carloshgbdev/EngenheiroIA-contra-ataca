from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.service.consumer import run_consumer
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_event_loop()
    loop.create_task(run_consumer())
    yield

app = FastAPI(
    title="Log Service",
    version="2.0.0",
    lifespan=lifespan,
)
