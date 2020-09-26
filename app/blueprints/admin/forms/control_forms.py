from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError


class ControlDetailForm(FlaskForm):
    date_start_day = DateField(u'Datum:', format='%d', validators=[DataRequired(), ])
    date_start_month = DateField(format='%m', validators=[DataRequired(), ])
    date_start_year = DateField(format='%Y', validators=[DataRequired(), ])
    time_start_hour = TimeField(u'Uhrzeit:', format='%H', validators=[DataRequired(), ])
    time_start_minute = TimeField(format='%M', validators=[DataRequired(), ])
    time_start_second = TimeField(format='%S', validators=[DataRequired(), ])
    date_end_day = DateField(u'Datum:', format='%d', validators=[DataRequired(), ])
    date_end_month = DateField(format='%m', validators=[DataRequired(), ])
    date_end_year = DateField(format='%Y', validators=[DataRequired(), ])
    time_end_hour = TimeField(u'Uhrzeit:', format='%H', validators=[DataRequired(), ])
    time_end_minute = TimeField(format='%M', validators=[DataRequired(), ])
    time_end_second = TimeField(format='%S', validators=[DataRequired(), ])
    reason = TextAreaField(validators=[DataRequired(), ])
    submit = SubmitField(u'Erstellen')

    def validate_date(self):
        end_date = datetime(self.date_end_year.data, self.date_end_month.data, self.date_end_day.data,
                            self.time_end_hour.data, self.time_end_minute.data, self.time_end_second.data)
        start_date = datetime(self.date_start_year.data, self.date_start_month.data, self.date_start_day.data,
                              self.time_start_hour.data, self.time_start_minute.data, self.time_start_second.data)
        print(end_date)
        print(start_date)
        if (end_date - start_date) < 0:
            raise ValidationError('Das Datum, an dem Ausgestempelt wurde,'
                                  'darf nicht hinter dem Datum liegen, an dem Eingestempelt wurde')