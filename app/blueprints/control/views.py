from flask import (
    render_template
)
from app.blueprints.control import control


@control.route('/', methods=['GET', 'POST'])
def main():
    return render_template('control/timeControl.html', title="Zeiterfassung")


@control.route('/<id>/', methods=['GET', 'POST'])
def timeview():
    return "under construction"
