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
            flash('Benutzer nicht aktiviert', 'warning')
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
        if action == 'Ausstempeln':
            if current_user.is_clocked:

                current_user.is_clocked = False
                controls = Control.query.filter(Control.user_id == current_user.user_id).all()
                for control in controls:
                    if control.time_end is None and current_user.clock_time is not None:
                        control.time_end = datetime.now()
                        db.session.commit()
                        current_user.is_clocked = False
                        return render_template('clock/clockin.html',
                                               title="Arbeitszeiten",
                                               sysmessages=True,
                                               route=request.path
                                               )
    controls = Control.query.filter(Control.user_id == current_user.user_id).all()
    current_time = None
    logged_time = None
    for control in controls:
        if control.time_end is None and current_user.clock_time is not None:
            current_time = control.time_start
            logged_time = get_time_difference(control.control_id, True)
    return render_template('clock/clockin.html',
                           title="Arbeitszeiten",
                           sysmessages=True,
                           time=current_time,
                           route=request.path,
                           logged=logged_time,
                           )


def get_time_difference(control_id, clocked=False):
    seconds_in_day = 24 * 60 * 60
    item = Control.query.get(control_id)
    if not clocked:
        difference = item.time_end - item.time_start
    else:
        difference = datetime.now() - item.time_start
    clock_in_minutes = divmod(difference.days * seconds_in_day + difference.seconds, 60)
    clock_in_hours = divmod(clock_in_minutes[0], 60)
    clock_in_time = '{} Stunden  {} Minuten'.format(clock_in_hours[0], clock_in_minutes[0] % 60)
    return clock_in_time
