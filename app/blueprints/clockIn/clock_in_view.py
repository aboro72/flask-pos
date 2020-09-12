from datetime import datetime
from flask import (
    flash,
    redirect,
    url_for,
    render_template
)
from flask_login import current_user
from app.blueprints.clockIn import clock_in


@clock_in.before_app_request
def before_request():
    if current_user.is_authenticated:
        if not current_user.is_active:
            flash('Benutzer nicht aktiviert', 'WARNING')
            redirect(url_for('main.index'))


@clock_in.route('/time')
def time():
    return render_template('clock/clockin.html', title="Arbeitszeiten")
