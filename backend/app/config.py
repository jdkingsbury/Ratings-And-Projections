from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    DATABASE_URL: str

    class Config:
        env_file = "../.env"

settings = Settings()
print(f"Settings loaded: {settings.dict()}")
