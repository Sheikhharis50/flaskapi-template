from enum import Enum
import logging


class LoggerEnum(Enum):
    error = logging.error
    info = logging.info
    warn = logging.warn
    debug = logging.debug
    critical = logging.critical
