from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    RABBITMQ_HOST: str = "rabbitmq"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "carlos"
    RABBITMQ_PASSWORD: str = "12345"
    PROJECT_NAME: str = "Client Service"
    API_VERSION: str = "v2"

    class Config:
        env_file = ".env"

settings = Settings()
