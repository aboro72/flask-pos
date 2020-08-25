from flask import (
    render_template,
)
from flask_login import login_required

from app.blueprints.control import control


@control.route('/', methods=['GET', 'POST'])
@login_required
def main():
    return render_template('control/timeControl.html', title="Zeiterfassung")


@control.route('/<id>/', methods=['GET', 'POST'])
@login_required
def timeview():
    return "under construction"
