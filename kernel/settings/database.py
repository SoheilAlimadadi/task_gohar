from .base import config


# Mongodb Host and Port
MONGO_HOST: str = config.get_value('mongodb', 'HOST')
MONGO_PORT: int = config.get_value('mongodb', 'PORT')

# Database and collection names
MONGO_DBS: dict = config.get_value('mongodb.databases')
