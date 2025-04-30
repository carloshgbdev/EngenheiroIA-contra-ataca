from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import os

DATABASE_URL = os.getenv('DATABASE_URL')

# Cria o engine assíncrono para conexão com o PostgreSQL
engine = create_async_engine(DATABASE_URL, echo=True)

# Cria a base para os modelos
Base = declarative_base()

# Criando o SessionLocal para obter sessões
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Função para obter uma sessão de banco de dados
async def get_db():
    async with SessionLocal() as session:
        yield session