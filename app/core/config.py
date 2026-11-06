from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    llm_api_key: str
    model_name: str = "gpt-6-luna"
    llm_base_url: str = "https://api.openai.com/v1"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()