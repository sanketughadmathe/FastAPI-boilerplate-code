from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = True

    model_config = {
        "env_file": ".env",
        "extra": "ignore",
    }


settings = Settings()
