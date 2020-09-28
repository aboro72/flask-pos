from app import db
from app.blueprints.admin import admin
from app.blueprints.admin.forms.control_forms import ControlDetailForm
from app.helper.decorator import manager_required
from app.models.control import Control
from app.models.modify import TimeModifyReason
from app.models.user import User
from datetime import datetime
from flask import (
    render_template,
    redirect,
    flash,
    url_for,
    request,
    json
)
from flask_login import login_required, current_user


@admin.route('/control/', methods=['GET'])
@login_required
@manager_required
def control():
    months = None
    control_list = Control.query.all()
    today_list = get_current_clock_in_times(control_list)
    now_date = (datetime.now().year, datetime.now().month)
    year_list = get_years_list(control_list, None)
    print(year_list[0])
    return render_template(
        'admin/control/control-index.html',
        title="Arbeitszeiten verwalten",
        today=today_list,
        current_date=now_date,
        years=year_list,
        months=months,
    )


@admin.route('/control/<year>/<month>/', methods=['GET'])
@login_required
@manager_required
def control_with_year_and_month(year, month):
    control_list = Control.query.all()
    current_list = get_clock_in_times(control_list, year, month)
    return render_template(
        'admin/control/parts/control-view.html',
        title="Arbeitszeiten Details - {}.{}".format(month, year),
        current=current_list,
        year=year,
        month=month
    )


@admin.route('/control/<name>/clock_out/', methods=['GET', 'POST'])
@login_required
@manager_required
def clock_out(name):
    if name is not None:
        user = User.query.filter_by(username=name).first()
        controls = Control.query.filter(Control.user_id == user.user_id).all()
        current_time = datetime.now()
        for control in controls:
            if control.time_end is None:
                control.time_end = current_time
                control.modified_at = current_time
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
                message = '<{}, {} {}> erfolgreich ausgeloggt'.format(user.uuid, user.firstname, user.lastname)
                flash(message, 'success')
                return redirect(url_for('admin.control'))
    flash('Mitarbeiter konnte nicht gefunden werden', 'warning')
    return redirect(url_for('admin.control'))


@admin.route('/control/<year>/', methods=['GET', ])
def view_control_year(year):
    flash('Noch nicht implementiert', 'info')
    return redirect(url_for('admin.control'))


@admin.route('/control/<year>/<month>/<name>/<time>/', methods=['GET', 'POST'])
def view_control_details(year, month, name, time):
    # get form
    form = ControlDetailForm()

    # get necessary info
    user = User.query.filter(User.username == name).first()
    details = get_control_time(month, year, user, time)

    # if form is submitted
    if request.method == 'POST':
        # if form is valid
        if form.validate_on_submit():

            # transform the form datetime objects
            end_date = date_object_to_datetime(
                form.date_end_year.data,
                form.date_end_month.data,
                form.date_end_day.data,
                form.time_end_hour.data,
                form.time_end_minute.data,
                form.time_end_second.data
            )
            start_date = date_object_to_datetime(
                form.date_start_year.data,
                form.date_start_month.data,
                form.date_start_day.data,
                form.time_start_hour.data,
                form.time_start_minute.data,
                form.time_start_second.data
            )

            # if the start date before the end date is
            if (start_date < end_date) and (start_date <= datetime.now()):
                # if end_date is not behind the current date
                if end_date <= datetime.now():
                    # if details is not empty
                    if details:
                        change_control_event(details[0][0], start_date, end_date, form.reason.data)
                        flash('Zeit erfolgreich geändert', 'success')
                        # redirect to /admin/control
                        return redirect(url_for('admin.control'))
                    else:
                        flash('Zeit konnte nicht geändert werden', 'error')
                else:
                    flash('Das End-Datum ist hinter dem aktuellen Datum', 'warning')
            else:
                flash('Das Start-Datum ist hinter dem End-Datum', 'warning')
        else:
            # if form is not valid
            flash('Daten der Form sind nicht gültig. Bitte kontrollieren sie die Zeiten', 'warning')

    # if form is not submitted

    # if details is not empty
    if details:
        # assign the current dates in the control event
        starttime = details[0][0].time_start
        endtime = details[0][0].time_end

        # transform datetimes to single dates and times
        form.time_start_hour.data = starttime
        form.time_start_minute.data = starttime
        form.time_start_second.data = starttime
        form.date_start_day.data = starttime
        form.date_start_month.data = starttime
        form.date_start_year.data = starttime
        form.time_end_hour.data = endtime
        form.time_end_minute.data = endtime
        form.time_end_second.data = endtime
        form.date_end_day.data = endtime
        form.date_end_month.data = endtime
        form.date_end_year.data = endtime

        # /admin/control/<year>/<month>/<user>/<time>
        return render_template('admin/control/parts/control-detail-view.html',
                               form=form,
                               details=details,
                               user=user
                               )
    # If its not possible to load the time control event
    # redirect to /admin/control
    flash('Stempelzeit konnte nicht geladen werden. Bitte Support konkaktieren')
    return redirect(url_for('admin.control'))


# get specific clock depending on year and month
def get_clock_in_times(control_list, year, month):
    date_list = list()
    tstr = "%d.%m.%Y-%H:%M:%S"
    seconds_in_day = 24 * 60 * 60
    if year is None:
        year = datetime.now().year
    if month is None:
        month = datetime.now().month
    for element in control_list:
        element_user = User.query.get(element.user_id)
        if element_user is not None:
            if int(year) == element.time_start.year:
                if int(month) == element.time_start.month:
                    if element.time_end is not None:
                        time_start = datetime.strftime(element.time_start, tstr)
                        time_end = datetime.strftime(element.time_end, tstr)
                        difference = element.time_end - element.time_start
                        clock_in_minutes = divmod(difference.days * seconds_in_day + difference.seconds, 60)
                        clock_in_hours = divmod(clock_in_minutes[0], 60)
                        clock_in_time = '{} Stunden  {} Minuten  {} Sekunden'.format(clock_in_hours[0],
                                                                                     clock_in_minutes[0] % 60,
                                                                                     clock_in_minutes[1])
                        date_list.append((
                            element_user,
                            time_start,
                            time_end,
                            clock_in_time,
                        ))
    return date_list


# get all user who currently clocked in
def get_current_clock_in_times(control_list):
    date_list = list()
    seconds_in_day = 24 * 60 * 60
    time_str = "%d.%m.%Y-%H:%M:%S"
    for element in control_list:
        element_user = User.query.get(element.user_id)
        if element_user is not None:
            if element.time_end is None:
                if current_user.role.permissions >= element_user.role.permissions:
                    time_start = datetime.strftime(element.time_start, time_str)
                    difference = datetime.now() - element.time_start
                    clock_in_minutes = divmod(difference.days * seconds_in_day + difference.seconds, 60)
                    clock_in_hours = divmod(clock_in_minutes[0], 60)
                    clock_in_time = '{} Stunden  {} Minuten  {} Sekunden'.format(clock_in_hours[0],
                                                                                 clock_in_minutes[0] % 60
                                                                                 , clock_in_minutes[1])
                    date_list.append((
                        element_user,
                        time_start,
                        clock_in_time,
                    ))
    return date_list


# get a list of all years where users are clocked in
def get_years_list(control_list, year):
    years = set()
    for element in control_list:
        if year is None:
            years.add(element.time_start.year)
        else:
            if element.time_start.year == year:
                years.add(element.time_start.year)
    mylist = list()
    for y in years:
        months = set()
        for item in control_list:
            if item.time_start.year == y:
                months.add(item.time_start.month)
        mylist.append((y, list(months)))
        months.clear()
    return mylist


# get a list of all month in a specific year where users are clocked in
def get_month_list(control_list, year, month):
    if year is None:
        year = datetime.now().year
    months = set()
    for element in control_list:
        if year == element.time_start.year:
            if month is None:
                months.add(element.time_start.month)
            else:
                if element.time_start.month == month:
                    months.add(element.time_start.month)
    return months


# get a specific control time
def get_control_time(month, year, user, time):
    if month is None or year is None or user is None or time is None:
        return None
    data_list = list()
    seconds_in_day = 24 * 60 * 60
    control_list = Control.query.filter(Control.user_id == user.user_id).all()
    for item in control_list:
        if int(year) == item.time_start.year:
            if int(month) == item.time_start.month and item.time_start.strftime("%d.%m.%Y-%H:%M:%S") == time:
                difference = item.time_end - item.time_start
                clock_in_minutes = divmod(difference.days * seconds_in_day + difference.seconds, 60)
                clock_in_hours = divmod(clock_in_minutes[0], 60)
                clock_in_time = '{} Stunden  {} Minuten  {} Sekunden'.format(clock_in_hours[0],
                                                                             clock_in_minutes[0] % 60
                                                                             , clock_in_minutes[1])
                # used a list for a single tuple    CHANGE NEEDED
                data_list.append((
                    item,
                    time,
                    clock_in_time
                ))
                return data_list
    return None


# create a datetime object from single dates and times
def date_object_to_datetime(year, month, day, hour, minute, second):
    int_year = int(year.year)
    int_month = int(month.month)
    int_day = int(day.day)
    int_hour = int(hour.hour)
    int_minute = int(minute.minute)
    int_second = int(second.second)
    date_time_object = datetime(
        int_year,
        int_month,
        int_day,
        int_hour,
        int_minute,
        int_second
    )
    return date_time_object


# Modify a control event with a new datetime
def change_control_event(control_event, start_date, end_date, modify_reason):
    # assign dates
    control_event.time_start = start_date
    control_event.time_end = end_date
    control_event.modified_at = datetime.now()
    control_event.is_modified = True

    # create a time modify reason
    time_modify_reason = TimeModifyReason(
        reason=modify_reason,
        control_by=control_event.control_id,
        created_at=datetime.now(),
        modified_user=control_event.user_id,
        modified_by=current_user.user_id
    )

    # add time modify reason to the database
    db.session.add(time_modify_reason)
    db.session.commit()
