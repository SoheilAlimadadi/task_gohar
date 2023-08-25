from motor.motor_asyncio import AsyncIOMotorClient

from utils.designs import Singleton
from kernel.settings import MONGO_HOST, MONGO_PORT, MONGO_DBS


class Database(metaclass=Singleton):

    def __init__(self, host: str = MONGO_HOST, port: int = MONGO_PORT) -> None:
        self.client = self.create_client(host, port)
        self.databases = self.create_databases()
        self.collections = self.create_collections()

    def create_client(self, host, port) -> AsyncIOMotorClient:
        return AsyncIOMotorClient(host, port)

    def create_databases(self) -> dict:
        return {db: self.client[db] for db in MONGO_DBS.keys()}

    def create_collections(self) -> list:
        collections = list()
        for db, collections in MONGO_DBS.items():
            for collection in collections:
                collections.append(self.databases[db][collection])
        return collections
