import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from dotenv import dotenv_values
from utils.helpers import get_key_val

ENV = dotenv_values(".env")

APP_NAME = get_key_val(ENV, 'APP_NAME')

SECRET_KEY = get_key_val(ENV, 'SECRET_KEY')

if not SECRET_KEY:
    raise ValueError(f"No SECRET_KEY set for {APP_NAME} Application")
else:
    SECRET_KEY = bytes(str(SECRET_KEY), 'utf-8')

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Token Settings
TOKEN_TIME = 30  # in minutes
TOKEN_ALGORITHM = "HS256"

# Database Configurations
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(
    get_key_val(ENV, 'DB_USER'),
    get_key_val(ENV, 'DB_PASSWORD'),
    get_key_val(ENV, 'DB_HOST'),
    get_key_val(ENV, 'DB_PORT'),
    get_key_val(ENV, 'DB_NAME'),
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
