import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Food & Health Smart App"
    API_V1_STR: str = "/api/v1"
    
    # DB
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "food_health")
    SQLALCHEMY_DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
    
    # We will fallback to sqlite if postgres URL fails during transition
    USE_SQLITE_FALLBACK: bool = True
    SQLITE_URL: str = "sqlite:///./food_health.db"
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    
    # AI
    VERTEX_AI_PROJECT_ID: str = os.getenv("VERTEX_AI_PROJECT_ID", "dummy-project")
    VERTEX_AI_LOCATION: str = os.getenv("VERTEX_AI_LOCATION", "us-central1")

    class Config:
        case_sensitive = True

settings = Settings()
