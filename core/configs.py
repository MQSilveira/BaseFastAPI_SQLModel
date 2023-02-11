from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://marcos:root@localhost:5433/postgres'
    
    class Config:
        case_sesitive = True

settings = Settings()


