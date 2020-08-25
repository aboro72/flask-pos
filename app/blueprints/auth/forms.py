from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Benutzername:', validators=[DataRequired()])
    password = PasswordField('Passwort:',  validators=[DataRequired()])
    submit = SubmitField('Login')
