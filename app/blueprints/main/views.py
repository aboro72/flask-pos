from datetime import datetime

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

from app.models.message import SystemNotification, NewsMessage


@main.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@main.route('/')
def to_index():
    return redirect(url_for('main.index'))


@main.route('/index/')
def index():
    newsletter = NewsMessage.query.all()
    return render_template('main/index.html',
                           title="Hauptseite",
                           sysmessages=True,
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
                           sysmessages=True,
                           route=request.path
                           )


@main.route('/notification')
@login_required
def notification():
    notes = get_messages()
    return jsonify([{
        'title': n.title,
        'data': n.body,
        'fc': n.fc,
        'bc': n.bc,
    } for n in notes])


def get_messages():
    messages = SystemNotification.query.all()
    notes = list()
    for i in messages:
        d = datetime.now()
        if i.is_repeatable:
            i.start_datetime = datetime(d.year, d.month, d.day, i.hour if i.hour > -1 else d.hour,
                                        i.minute if i.minute > -1 else d.minute)
            i.end_datetime = datetime(d.year, d.month, d.day, i.hour if i.hour > -1 else d.hour,
                                      (i.minute + i.duration) if i.minute > -1 else d.minute)
        else:
            i.start_datetime = datetime(i.year, i.month, i.day, i.hour, i.minute)
            i.end_datetime = datetime(i.year, i.month, i.day, i.hour, i.minute + i.duration)
        if i.start_datetime <= d <= i.end_datetime:
            notes.append(i)
    return notes
