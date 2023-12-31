import tomllib
import logging.config
import logging

from .base import (
    BASE_DIR,
    config
)
from utils.funcs import create_directories

def setup_logging():
    """
    Create directories related to logging
    Read logging config from loggin.toml
    """
    DIRECTORIES = config.get_value("logging", 'LOG_DIRS')
    create_directories(BASE_DIR, DIRECTORIES)

    with open(f'{BASE_DIR}/configs/logging/logging.toml', mode='rb') \
        as config_file:
        log_conf_dict = tomllib.load(config_file)
        logging.config.dictConfig(log_conf_dict)
