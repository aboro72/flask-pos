from datetime import datetime
from app import db

from flask import (
    render_template,
    session,
    current_app as app,
    request,
    redirect,
    url_for,
    jsonify,
)
from flask_login import login_required

from app.blueprints.main import main

from app.models.message import SystemNotification


@main.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@main.route('/')
def to_index():
    return redirect(url_for('main.index'))


@main.route('/index/')
def index():
    newsletter = list()
    newsletter.append('Flask-Pos hat jetzt Nachrichten zum wegklicken')
    newsletter.append('Noch eine Nachricht... Das hört ja gar nicht mehr auf')
    newsletter.append('Diesmal eine mehrzeilige Nachricht...<br>Das wird ja immer besser...'
                      '<br>Das hört ja gar nicht mehr auf')
    return render_template('main/index.html',
                           title="Hauptseite",
                           username=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.time,
                           route=request.path,
                           newsletter=newsletter
                           )


@main.route('/contact/')
def contact():
    return render_template('main/contact.html',
                           title="Kontakt",
                           route=request.path
                           )


@main.route('/notifications')
@login_required
def notifications():
    notes = get_messages()
    return jsonify([{
        'data': n.body,
        'hour': (datetime.now().hour - n.end_datetime.hour),
        'minute': (datetime.now().minute - n.end_datetime.minute)
    } for n in notes])


def get_messages():
    messages = SystemNotification.query.all()
    notes = list()
    gettime = datetime.now()
    for item in messages:
        if item.is_repeatable:
            if item.start_datetime.hour <= gettime.hour <= item.end_datetime.hour:
                if item.start_datetime.minute <= gettime.minute <= item.end_datetime.minute:
                    notes.append(item)
        else:
            if item.start_datetime <= gettime <= item.end_datetime:
                notes.append(item)
    return notes
