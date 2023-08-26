import logging

from fastapi import FastAPI

from database.core import Database
from users.api.v1 import user_router

app = FastAPI()
dbLogger = logging.getLogger('database')

@app.on_event('startup')
async def connect_db():
    """
    Connect the database on startup event
    """
    Database()
    dbLogger.info("Connected to the database successfully.")


app.include_router(
    user_router,
    tags=["Teams"],
    prefix="/v1"
)
