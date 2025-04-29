from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str ="mongodb://carlos:12345@mongodb:27017/"
    MONGO_DB_NAME: str = "logdb"

    model_config = {
        "env_file": ".env",
    }

settings = Settings()
