import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import dotenv_values
from utils.helpers import get_key_val

ENV = dotenv_values(".env")

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

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
