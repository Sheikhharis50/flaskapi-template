from dotenv import dotenv_values
import os
from utils.helpers import getKeyVal

ENV = dotenv_values(".env")

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(
    getKeyVal(ENV, 'DB_USER'),
    getKeyVal(ENV, 'DB_PASSWORD'),
    getKeyVal(ENV, 'DB_HOST'),
    getKeyVal(ENV, 'DB_PORT'),
    getKeyVal(ENV, 'DB_NAME'),
)

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
