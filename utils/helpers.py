import os
from .enums import LoggerEnum
from datetime import datetime


def get_key_val(d: dict = {}, key: str = ''):
    return d.get(key)


def get_env_val(key: str):
    return os.getenv(key)


def serialize_all(obj_list: list = []):
    '''
    @obj_list list(Models)
    '''
    data = []
    try:
        data = [obj.serialize() for obj in obj_list]
    except Exception as e:
        pass
    return data


def log(message: str = '', level: str = 'error'):
    match level:
        case "error":
            logger = LoggerEnum.error
        case "info":
            logger = LoggerEnum.info
        case "warn":
            logger = LoggerEnum.warn
        case "debug":
            logger = LoggerEnum.debug
        case "critical":
            logger = LoggerEnum.critical
        case _:
            logger = LoggerEnum.info

    logger(
        "[%s][%s]: %s" %
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            str(level).upper(), str(message)
        )
    )
