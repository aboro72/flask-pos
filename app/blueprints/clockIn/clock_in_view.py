from datetime import datetime
from flask import (
    flash,
    redirect,
    url_for,
    render_template,
    request
)

from flask_login import current_user

from app import db
from app.models.user import User
from app.models.control import Control
from app.helper.decorator import user_required
from app.blueprints.clockIn import clock_in


@clock_in.before_app_request
def before_request():
    if current_user.is_authenticated:
        if not current_user.is_active:
            flash('Benutzer nicht aktiviert', 'WARNING')
            redirect(url_for('main.index'))


@clock_in.route('/', methods=['GET', 'POST'])
@user_required
def time():
    if request.method == 'POST':
        action = request.form.get("clockin")
        if action == 'Einstempeln':
            if not current_user.is_clocked:
                user = User.query.filter_by(user_id=current_user.user_id).first()
                current_user.is_clocked = True
                clocktime = datetime.now()
                control = Control(
                    created_at=clocktime,
                    is_modified=False,
                    time_start=clocktime,
                )
                control.user_id = current_user.user_id
                user.clock_time = clocktime
                db.session.add(control)
                db.session.commit()
                current_user.is_clocked = True
                flash("Benutzer " + current_user.username + " erfolgreich eingestempelt")
        if action == 'Ausstempeln':
            if current_user.is_clocked:

                current_user.is_clocked = False
                controls = Control.query.filter(Control.user_id == current_user.user_id).all()
                for control in controls:
                    if control.time_end is None and current_user.clock_time is not None:
                        control.time_end = datetime.now()
                        db.session.commit()
                        current_user.is_clocked = False
                        flash("Benutzer " + current_user.username + " erfolgreich ausgestempelt")
                        return render_template('clock/clockin.html', title="Arbeitszeiten")
    controls = Control.query.filter(Control.user_id == current_user.user_id).all()
    current_time = None
    for control in controls:
        if control.time_end is None and current_user.clock_time is not None:
            current_time = control.time_start.strftime('%d.%m.%Y, %H:%M:%S')
    return render_template('clock/clockin.html', title="Arbeitszeiten", time=current_time)
