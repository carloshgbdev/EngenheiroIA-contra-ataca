from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CLIENT_SERVICE_URL: str = "http://client_service:8001/v1/clients"
    ANALYTICS_SERVICE_URL: str = "http://analytics_service:8002/v1/analytics"
    CHATBOT_SERVICE_URL: str = "http://chatbot_service:8003/v1/chatbot"

    class Config:
        env_file = ".env"

settings = Settings()
