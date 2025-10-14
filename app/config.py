from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    ALLOW_ORIGINS: str = '*'
    OPENAI_API_KEY: str = os.environ['OPENAI_API_KEY']
    MODEL: str = os.environ['MODEL']
    TOKENIZER_ENCODING: str = 'o200k_base'
    EMBEDDING_MODEL: str = 'text-embedding-3-large'
    EMBEDDING_DIMENSIONS: int = 1024
    REDIS_HOST: str = os.environ['REDIS_HOST'] #= '10.0.2.4'
    REDIS_PORT: int = 6379
    DOCS_DIR: str = os.environ['DOCS_DIR'] #'data/docs'
    EXPORT_DIR: str = 'data'
    VECTOR_SEARCH_TOP_K: int = 10

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()