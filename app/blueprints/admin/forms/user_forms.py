from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError

from app.models.user import User


class UserAddForm(FlaskForm):
    username = StringField('Benutzername:', validators=[DataRequired(message="Bitte Benutzernamen angeben"), ])
    email = StringField('Email:', validators=[DataRequired(), Email(), ])
    firstname = StringField('Vorname:', validators=[DataRequired(), ])
    lastname = StringField('Nachname:', validators=[DataRequired(), ])
    uuid = StringField('Mitarbeiter-Id:', validators=[DataRequired(), ])
    role = SelectField('Rolle:', coerce=int, choices=[])
    submit = SubmitField('Erstellen')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email ist schon vorhanden")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Benutzername ist schon vorhanden")

    def validate_uuid(self, field):
        if User.query.filter_by(uuid=field.data).first():
            raise ValidationError("Mitarbeiter-Id ist schon vorhanden")


class UserEditForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    firstname = StringField('Vorname:', validators=[DataRequired(), Email(), ])
    lastname = StringField('Nachname:', validators=[DataRequired(), ])
    uuid = StringField('Mitarbeiter-Id:', validators=[DataRequired(), ])
    role = SelectField('Rolle:', coerce=int, choices=[])
    submit = SubmitField('Ändern')

    def validate_email(self, field):
        current_email = User.query.filter(email=field.data).first()
        if current_email is not None:
            if current_email is not current_user.email:
                raise ValidationError("Email ist schon vorhanden")

    def validate_uuid(self, field):
        current_uuid = User.query.filter_by(uuid=field.data).first()
        if current_uuid is not None:
            if current_uuid is not current_user.uuid:
                raise ValidationError("Mitarbeiter-Id ist schon vorhanden")