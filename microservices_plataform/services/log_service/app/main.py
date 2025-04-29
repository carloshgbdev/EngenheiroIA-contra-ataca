from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🌟 LIFESPAN STARTED 🌟")
    yield
    print("🌙 LIFESPAN SHUTDOWN 🌙")


print("Iniciando o aplicativo FastAPI...")

app = FastAPI(
    title="Log Service",
    version="2.0.0",
    lifespan=lifespan,
)
