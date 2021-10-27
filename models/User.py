from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from config import Session, SECRET_KEY, TOKEN_TIME, TOKEN_ALGORITHM
from sqlalchemy import or_, and_
import jwt
from datetime import datetime, timedelta

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.String(255))
    address = db.Column(db.String(255))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'age': self.age,
            'address': self.address,
        }

    @staticmethod
    def gen_jwt_token(user: object = None) -> str:
        return jwt.encode(
            {
                'public_id': user.public_id,
                'exp': datetime.utcnow() + timedelta(minutes=TOKEN_TIME)
            },
            SECRET_KEY,
            algorithm=TOKEN_ALGORITHM
        )

    @staticmethod
    def auth_user(username: str = None, password: str = None):
        user = User.check_if_exist(username=username)
        if not user:
            return None, 'User does not exist!'
        elif user and check_password_hash(user.password, password):
            return user, 'User is authenticated.'
        return None, 'Wrong password!'

    @staticmethod
    def check_if_exist(email: str = None, username: str = None):
        if username and email:
            conditions = or_(
                User.email == email,
                User.username == username
            )
        elif username:
            conditions = User.username == username
        elif email:
            conditions = User.email == email

        return Session.query(User).filter(conditions).scalar()
