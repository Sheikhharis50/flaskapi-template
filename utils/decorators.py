from flask import request
from config import SECRET_KEY, TOKEN_ALGORITHM
from models.User import User
import jwt
from functools import wraps
from utils.response import APIResponse


def token_required(provide_user: bool = False):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'token' in request.headers:
                token = request.headers['token']
            if not token:
                return APIResponse(
                    dict(status='missing', message='Token is missing!'),
                    401
                )
            try:
                data = jwt.decode(
                    token,
                    SECRET_KEY,
                    algorithms=[TOKEN_ALGORITHM]
                )
                if provide_user:
                    current_user = User.query\
                        .filter_by(public_id=data.get('public_id', ''))\
                        .first()
                    return f(current_user, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                return APIResponse(
                    dict(status='expired', message='Token is expired!'),
                    401
                )
            except:
                return APIResponse(
                    dict(status='invalid', message='Token is invalid!'),
                    401
                )
            return f(*args, **kwargs)
        return decorated
    return wrapper


def catch(func, callback=None):
    '''
    Decorator for catching exceptions
    '''

    def wrap_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
            if callback:
                callback()
    return wrap_function
