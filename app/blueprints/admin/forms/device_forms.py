from flask import current_app as app
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app.models.device import Device


class DeviceAddForm(FlaskForm):
    label = StringField('Bezeichnung:', validators=[DataRequired(message="Bitte Gerätenamen angeben"), ])
    uuid = StringField('Geräte-Id:', validators=[DataRequired(), ])
    serial = StringField('Seriennummer:', validators=[DataRequired(), ])
    manufacturer = StringField('Hersteller:', validators=[DataRequired(), ])
    order_from = StringField('Gekauft bei', validators=[DataRequired(), ])
    submit = SubmitField('Erstellen')

    def validate_serial_number(self, field):
        if Device.query.filter_by(serial_number=field.data).first():
            raise ValidationError("Seriennummer ist schon vorhanden")

    def validate_uuid(self, field):
        if Device.query.filter_by(uuid=field.data).first():
            raise ValidationError("Geräte-Id ist schon vorhanden")


class DeviceEditForm(FlaskForm):
    label = StringField('Bezeichnung:', validators=[DataRequired(message="Bitte Gerätenamen angeben"), ])
    uuid = StringField('Geräte-Id:', validators=[DataRequired(), ])
    serial = StringField('Seriennummer:', validators=[DataRequired(), ])
    manufacturer = StringField('Hersteller:', validators=[DataRequired(), ])
    ordered_from = StringField('Gekauft bei', validators=[DataRequired(), ])
    submit = SubmitField('Ändern')

    def validate_serial_number(self, field):
        if field.data is not app._get_current_object().serial_number:
            if Device.query.filter(Device.serial_number == field.data).first() is None:
                raise ValidationError("Seriennummer existiert bereits")

    def validate_uuid(self, field):
        if field.data is not app._get_current_object().uuid:
            if Device.query.filter(Device.uuid == field.data).first() is None:
                raise ValidationError("Geräte-Id existiert bereits")