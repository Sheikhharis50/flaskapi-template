from flask import request
from models.User import User
from forms.UserForm import UserForm
from utils.helpers import serialize_all
from utils.decorators import token_required
from utils.response import APIResponse
from config import Session


@token_required()
def get_users():
    data = serialize_all(Session.query(User).all())
    return APIResponse(data)


def get_user(user_id: int):
    user = Session.query(User).filter_by(id=user_id).scalar()
    if user:
        return APIResponse(user.serialize())
    return APIResponse(dict(message='Not Found!'), 404)


def update_user(user_id: int):
    user = Session.query(User).filter_by(id=user_id).scalar()
    if user:
        f = UserForm(request.form)
        valid, message = f.validate(user_id=user_id)
        if valid:
            form_data = f.get_form_data()
            user.first_name = form_data['first_name']
            user.last_name = form_data['last_name']
            user.age = form_data['age']
            user.address = form_data['address']
            Session.commit()
            return APIResponse(user.serialize())
        return APIResponse(dict(message=message), 406)
    return APIResponse(dict(message='Not Found!'), 404)


def delete_user(user_id):
    user = Session.query(User).filter_by(id=user_id).scalar()
    if user:
        Session.delete(user)
        Session.commit()
        return APIResponse(dict(message='Deleted.'))
    return APIResponse(dict(message='Not Found!'), 404)
