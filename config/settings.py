import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # URLs
    BASE_URL = os.getenv("BASE_URL")
    
    
    # Browser config
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "500"))
    BROWSER_TIMEOUT = int(os.getenv("BROWSER_TIMEOUT", "10000"))
    

settings = Settings()