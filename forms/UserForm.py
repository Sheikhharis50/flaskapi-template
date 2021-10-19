from enum import Flag
from sqlalchemy.sql.elements import and_
from sqlalchemy.sql.expression import false
import wtforms as forms
from models.User import User
from config import Session
from sqlalchemy import or_, and_


class UserForm(forms.Form):
    username = forms.StringField(
        'Username', [
            forms.validators.Length(min=4, max=25),
            forms.validators.DataRequired()
        ]
    )
    email = forms.StringField(
        'Email Address', [
            forms.validators.Length(min=6, max=35),
            forms.validators.DataRequired(),
            forms.validators.Email()
        ]
    )
    first_name = forms.StringField(
        'First Name', [
            forms.validators.Length(min=1),
            forms.validators.DataRequired()
        ]
    )
    last_name = forms.StringField(
        'Last Name', [
            forms.validators.Length(min=1),
            forms.validators.DataRequired()
        ]
    )
    age = forms.IntegerField('Age')
    address = forms.TextField('address')

    def validate(self, extra_validators=None, user_id: int = 0):
        condition = or_(
            User.username == self.username.data,
            User.email == self.email.data
        )
        if user_id:
            condition = and_(condition, User.id != user_id)
        query = Session.query(User).filter(condition)
        if query.count():
            return False, 'User already exists!'
        return super().validate(extra_validators=extra_validators), 'Saved!'
