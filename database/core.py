import logging
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection
)
from utils.designs import Singleton
from kernel.settings import MONGO_HOST, MONGO_PORT, MONGO_DBS


databaseLogger = logging.getLogger("database")

class Database(metaclass=Singleton):
    """
    A singleton class for managing MongoDB connections and collections.

    Parameters:
        host (str): The MongoDB server host. Defaults to MONGO_HOST from
        settings.
        port (int): The MongoDB server port. Defaults to MONGO_PORT
        from settings.

    Attributes:
        client (AsyncIOMotorClient): The MongoDB client instance.
        databases (dict): A dictionary of MongoDB databases, with database
        names as keys and AsyncIOMotorDatabase instances as values.
        collections (dict): A dictionary of MongoDB collections, with
        collection names as keys and AsyncIOMotorCollection instances
        as values.

    """

    def __init__(self, host: str = MONGO_HOST, port: int = MONGO_PORT) -> None:
        """
        Initialize the Database instance.

        Args:
            host (str): The MongoDB server host. Defaults to MONGO_HOST from
            settings.
            port (int): The MongoDB server port. Defaults to MONGO_PORT from
            settings.

        """
        self.client = self.create_client(host, port)
        self.databases = self.create_databases()
        self.collections = self.create_collections(self.databases)

    def create_client(self, host: str, port: int) -> AsyncIOMotorClient:
        """
        Create a MongoDB client instance.

        Args:
            host (str): The MongoDB server host.
            port (int): The MongoDB server port.

        Returns:
            AsyncIOMotorClient: The MongoDB client instance.

        """
        return AsyncIOMotorClient(host, port)

    def create_databases(self) -> dict[str, AsyncIOMotorDatabase]:
        """
        Create MongoDB databases.

        Returns:
            dict: A dictionary of MongoDB databases, with database names as
            keys and AsyncIOMotorDatabase instances as values.

        """
        databases = {db: self.client[db] for db in MONGO_DBS.keys()}
        databaseLogger.info("Databases created")
        return databases

    def create_collections(
            self,
            databases: dict
    ) -> dict[str, AsyncIOMotorCollection]:
        """
        Create MongoDB collections.

        Args:
            databases (dict): A dictionary of MongoDB databases, with
            database names as keys and AsyncIOMotorDatabase instances
            as values.

        Returns:
            dict: A dictionary of MongoDB collections, with collection names
            as keys and AsyncIOMotorCollection instances as values.

        """
        collections_dict: dict[str, AsyncIOMotorCollection] = dict()
        for db, collections in MONGO_DBS.items():
            for collection_name in collections:
                collections_dict[collection_name] =  \
                    databases[db][collection_name]
                databaseLogger.info(f"collection '{collection_name}' created")
        return collections_dict
