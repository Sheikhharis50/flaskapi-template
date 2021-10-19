import os


def getKeyVal(d: dict = {}, key: str = ''):
    return d.get(key)


def getEnvVal(key: str):
    return os.getenv(key)
