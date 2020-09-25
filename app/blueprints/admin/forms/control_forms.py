from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError


class ControlDetailForm(FlaskForm):
    date_start_day = DateField('Datum:', format='%d', validators=[DataRequired(), ])
    date_start_month = DateField(format='%m', validators=[DataRequired(), ])
    date_start_year = DateField(format='%Y', validators=[DataRequired(), ])
    time_start_hour = TimeField('Uhrzeit:', format='%H', validators=[DataRequired(), ])
    time_start_minute = TimeField(format='%M', validators=[DataRequired(), ])
    time_start_second = TimeField(format='%S', validators=[DataRequired(), ])
    date_end_day = DateField('Datum:', format='%d', validators=[DataRequired(), ])
    date_end_month = DateField(format='%m', validators=[DataRequired(), ])
    date_end_year = DateField(format='%Y', validators=[DataRequired(), ])
    time_end_hour = TimeField('Uhrzeit:', format='%H', validators=[DataRequired(), ])
    time_end_minute = TimeField(format='%M', validators=[DataRequired(), ])
    time_end_second = TimeField(format='%S', validators=[DataRequired(), ])
    reason = TextAreaField(validators=[DataRequired(), ])
    submit = SubmitField('Erstellen')
