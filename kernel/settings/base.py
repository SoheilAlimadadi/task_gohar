from pathlib import Path

from utils.dynamic_settings import config

# project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# FastAPI host and port
FAST_HOST = config.get_value("fastapi", 'HOST')
FAST_PORT = config.get_value("fastapi", "PORT")
