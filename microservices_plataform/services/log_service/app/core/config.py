from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Informações do RabbitMQ
    RABBITMQ_HOST: str = "rabbitmq"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "carlos"
    RABBITMQ_PASSWORD: str = "12345"
    
    # Informações do MongoDB
    MONGO_URL: str ="mongodb://carlos:12345@mongodb:27017/"
    MONGO_DB_NAME: str = "logdb"

    model_config = {
        "env_file": ".env",
    }

settings = Settings()
