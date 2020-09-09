from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField
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
    ve = HiddenField('ve')
    ud = HiddenField('ud')
    email = StringField('Email:', validators=[DataRequired()])
    firstname = StringField('Vorname:', validators=[DataRequired(), Email(), ])
    lastname = StringField('Nachname:', validators=[DataRequired(), ])
    uuid = StringField('Mitarbeiter-Id:', validators=[DataRequired(), ])
    role = SelectField('Rolle:', coerce=int, choices=[])
    submit = SubmitField('Ändern')

    def validate_email(self, field):
        if not field.data == self.ve.data:
            if User.query.filter(User.email == field.data).first():
                raise ValidationError("Email existiert bereits")

    def validate_uuid(self, field):
        if not field.data == self.ud.data:
            if User.query.filter(User.uuid == field.data).first():
                raise ValidationError("Mitarbeiter-Id existiert bereits")
