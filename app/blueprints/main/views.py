from datetime import datetime

from flask import (
    render_template,
    session,
    current_app as app,
    request
)
from app.blueprints.main import main


@main.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@main.route('/')
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
