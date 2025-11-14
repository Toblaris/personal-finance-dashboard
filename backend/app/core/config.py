from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    ENV: str = "development"
    DATABASE_URL: str | None = None
    NORDIGEN_SECRET_ID: str | None = None
    NORDIGEN_SECRET_KEY: str | None = None
    NORDIGEN_REDIRECT_URI: str | None = None
    ALLOWED_ORIGINS: List[str] = Field(default_factory=list)

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()