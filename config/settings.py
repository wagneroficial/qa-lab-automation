import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # URLs
    BASE_URL = os.getenv("BASE_URL")
    
    # Credenciais Admin
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
    
    # Credenciais User
    USER_EMAIL = os.getenv("USER_EMAIL") 
    USER_PASSWORD = os.getenv("USER_PASSWORD")
    
    # Browser config
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "500"))
    BROWSER_TIMEOUT = int(os.getenv("BROWSER_TIMEOUT", "10000"))
    
    @classmethod
    def validate(cls):
        """Valida se credenciais estão configuradas"""
        required = ["ADMIN_EMAIL", "ADMIN_PASSWORD"]
        missing = [var for var in required if not getattr(cls, var)]
        
        if missing:
            raise ValueError(f"Variáveis obrigatórias não configuradas: {missing}")

# Instanciar configurações
settings = Settings()