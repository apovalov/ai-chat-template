from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings

APP_TITLE = "Chatbot API"

class Settings(BaseSettings):
    llm_host: AnyUrl
    llm_name: str = Field(default="llama3.2")
    llm_api_key: str = Field(default="ollama")
    max_question_length: int = Field(default=512)

settings = Settings()

# Добавь отладку
print(f"🔍 DEBUG: LLM_HOST = {settings.llm_host}")
print(f"🔍 DEBUG: LLM_NAME = {settings.llm_name}")
print(f"🔍 DEBUG: LLM_API_KEY = {settings.llm_api_key}")

APP_TITLE = "Chatbot API"


class Settings(BaseSettings):
    llm_host: AnyUrl
    llm_name: str = Field(default="llama3.2")
    llm_api_key: str = Field(default="ollama")

    max_question_length: int = Field(default=512)


settings = Settings()
