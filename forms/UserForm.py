from .BaseForm import BaseForm, forms



class UserForm(BaseForm):
    username = forms.StringField(
        'Username', [
            forms.validators.Length(min=4, max=25),
            forms.validators.DataRequired(),
        ]
    )
    password = forms.PasswordField(
        'Password', [
            forms.validators.Length(min=8, max=100),
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
