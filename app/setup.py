from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # supabase_key: str
    # supabase_url: str
    # database_password:str
    # database_username: str
    # database_host:str
    database_connection: str
    class Config:
        env_file = ".env"

settings = Settings()