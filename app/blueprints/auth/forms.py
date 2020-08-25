from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Benutzername:', validators=[DataRequired()])
    password = PasswordField('Passwort:',  validators=[
        DataRequired(),
        # Length(8, 64),
    ])
    remember_me = BooleanField('Eingeloggt bleiben')
    submit = SubmitField('Login')
