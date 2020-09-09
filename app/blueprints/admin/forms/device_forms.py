from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, ValidationError

from app.models.device import Device


class DeviceAddForm(FlaskForm):
    label = StringField('Bezeichnung:', validators=[DataRequired(), ])
    uuid = StringField('Geräte-Id:', validators=[DataRequired(), ])
    serial = StringField('Seriennummer:', validators=[DataRequired(), ])
    manufacturer = StringField('Hersteller:', validators=[DataRequired(), ])
    ordered_from = StringField('Gekauft bei', validators=[DataRequired(), ])
    submit = SubmitField('Erstellen')

    def validate_serial(self, field):
        if Device.query.filter(Device.serial_number == field.data).first():
            raise ValidationError("Seriennummer ist schon vorhanden")

    def validate_uuid(self, field):
        if Device.query.filter(Device.device_uuid == field.data).first():
            raise ValidationError("Geräte-Id ist schon vorhanden")


class DeviceEditForm(FlaskForm):
    sn = HiddenField('sn')
    ud = HiddenField('ud')
    label = StringField('Bezeichnung:', validators=[DataRequired(), ])
    uuid = StringField('Geräte-Id:', validators=[DataRequired(), ])
    serial = StringField('Seriennummer:', validators=[DataRequired(), ])
    manufacturer = StringField('Hersteller:', validators=[DataRequired(), ])
    ordered_from = StringField('Gekauft bei', validators=[DataRequired(), ])
    submit = SubmitField('Ändern')

    def validate_serial(self, field):
        if not field.data == self.sn.data:
            if Device.query.filter(Device.serial_number == field.data).first():
                raise ValidationError("Seriennummer existiert bereits")

    def validate_uuid(self, field):
        if not field.data == self.ud.data:
            if Device.query.filter(Device.device_uuid == field.data).first():
                raise ValidationError("Geräte-Id existiert bereits")