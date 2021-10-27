from flask import request
from models.User import User
from forms.UserForm import UserForm
from forms.AuthForm import (LoginForm, RenewTokenForm)
from utils.response import APIResponse
from utils.decorators import token_required
from config import Session
import uuid
from werkzeug.security import generate_password_hash


def login():
    f = LoginForm(request.form)

    if f.validate():
        # parse form data
        form_data = f.get_form_data()

        # authenticate user
        user, message = User.auth_user(**form_data)
        if not user:
            return APIResponse(dict(message=message), 401)

        # generates the JWT Token
        token = User.gen_jwt_token(user)

        return APIResponse(
            dict(
                message='Login Successfully.',
                token=token
            )
        )
    return APIResponse(f.get_errors(), 406)


def signup():
    f = UserForm(request.form)
    if f.validate():
        # parse form data
        form_data = f.get_form_data()

        # check if user exists
        if User.check_if_exist(
            username=form_data.get('username'),
            email=form_data.get('email')
        ):
            return APIResponse(dict(message='User already exist!'), 406)

        # generate password
        password = form_data.get('password')
        form_data['password'] = generate_password_hash(password)
        # make object
        user = User(**form_data, public_id=str(uuid.uuid4()))
        # store object
        Session.add(user)
        Session.commit()
        return APIResponse(user.serialize())
    return APIResponse(f.get_errors(), 406)


def renew_token():
    f = RenewTokenForm(request.form)
    if f.validate():
        # parse form data
        form_data = f.get_form_data()

        # verify token
        res = token_required()(lambda x: x)(None)

        # authenticate user
        user = User.check_if_exist(
            email=form_data.get('username'),
            username=form_data.get('username'),
        )
        if not user:
            return APIResponse(dict(message='User does not exist!'), 401)

        if not res:
            return APIResponse(dict(message='Token is not expired yet!'), 406)

        res_json = res.get_json()
        if res_json.get('status') != 'expired':
            return APIResponse(dict(message=res_json.get('message')), 401)

        # generates the JWT Token
        token = User.gen_jwt_token(user)

        return APIResponse(dict(token=token))
    return APIResponse(f.get_errors(), 406)
