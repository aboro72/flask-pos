from datetime import datetime, date, timedelta
from flask import (
    render_template,
    redirect, flash, url_for,
)
from app.blueprints.admin import admin

from flask_login import login_required, current_user

from app import db
from app.helper.decorator import manager_required
from app.models.control import Control
from app.models.modify import TimeModifyReason
from app.models.user import User


@admin.route('/control/', methods=['GET', 'POST'])
@login_required
@manager_required
def control():
    control_list = Control.query.all()
    user_list = User.query.all()
    user_count = 0
    for user in user_list:
        if current_user.role.permissions >= user.role.permissions:
            if current_user.user_id != user.user_id:
                if user.is_clocked:
                    user_count += 1
    if user_count == 0:
        user_list = None
    month_list = get_times(control_list)
    today_list = get_clock_in_times(control_list)
    return render_template(
        'admin/control/control-index.html',
        title="Arbeitszeiten verwalten",
        controls=control_list,
        users=user_list,
        months=month_list,
        today=today_list,
        )


@admin.route('/control/<name>/clock_out/', methods=['GET', 'POST'])
@login_required
@manager_required
def clock_out(name):
    user = User.query.filter_by(username=name).first()
    controls = Control.query.filter(Control.user_id == user.user_id).all()
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    for control in controls:
        if control.time_end is None:
            control.time_end = current_time
            control.is_modified = True
            modify_reason = TimeModifyReason(
                reason="<{}, {} {}> wurde von <{}, {} {}> ausgestempelt".format(
                    user.uuid,
                    user.firstname,
                    user.lastname,
                    current_user.uuid,
                    current_user.firstname,
                    current_user.lastname,
                ),
                control_by=control.control_id,
                modified_by=current_user.user_id,
                modified_user=user.user_id,
                created_at=current_time
            )
            db.session.add(modify_reason)
            user.is_clocked = False
            db.session.commit()
            message = 'Mitarbeiter <{}, {} {}> erfolgreich ausgeloggt'.format(user.uuid, user.firstname, user.lastname)
            flash(message)
            return redirect(url_for('admin.control'))
    flash('Mitarbeiter konnte nicht gefunden werden')
    return redirect(url_for('admin.control'))


def get_times(control_list):
    date_list = list()
    tstr = "%d-%m-%Y %H:%M:%S"

    for element in control_list:
        if element.time_end is not None:

            if int(datetime.strftime(element.time_start, "%m")) == datetime.now().month:
                time_start = datetime.strftime(element.time_start, tstr)
                time_end = datetime.strftime(element.time_end, tstr)
                currentUser = User.query.get(element.user_id)
                if currentUser is None:
                    currentUser = 'unbekannter Nutzer'
                else:
                    currentUser = '{} {}'.format(currentUser.firstname, currentUser.lastname)
                date_list.append((
                    currentUser,
                    time_start,
                    time_end
                ))
    return date_list


def get_clock_in_times(control_list):
    date_list = list()
    tstr = "%d-%m-%Y %H:%M:%S"
    curdate = datetime.now()
    for element in control_list:
        if element.time_end is None:

            if int(datetime.strftime(element.time_start, "%m")) == datetime.now().month:
                time_start = datetime.strftime(element.time_start, tstr)
                currentUser = User.query.get(element.user_id)
                if currentUser is None:
                    currentUser = 'unbekannter Nutzer'
                else:
                    currentUser = '{} {}'.format(currentUser.firstname, currentUser.lastname)
                    difference = curdate - element.time_start
                    seconds_in_day = 24 * 60 * 60
                    timedelta(0, 8, 562000)
                    clock_in_time = divmod(difference.days * seconds_in_day + difference.seconds, 60)
                    clock_in_time = '{} Minuten  {} Sekunden'.format(clock_in_time[0], clock_in_time[1])
                date_list.append((
                    currentUser,
                    time_start,
                    clock_in_time,
                ))
    return date_list