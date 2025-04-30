from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CHATBOT_NAME: str = "Virtual Assistant"

    class Config:
        env_file = ".env"

settings = Settings()
