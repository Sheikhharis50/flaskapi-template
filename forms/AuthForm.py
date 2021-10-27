from .BaseForm import BaseForm, forms


class LoginForm(BaseForm):
    username = forms.StringField(
        'Username', [
            forms.validators.DataRequired()
        ]
    )
    password = forms.StringField(
        'Password', [
            forms.validators.DataRequired()
        ]
    )


class RenewTokenForm(BaseForm):
    username = forms.StringField(
        'Username', [
            forms.validators.DataRequired()
        ]
    )
