from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    nyt_api_key: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()