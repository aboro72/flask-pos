from flask import (
    render_template
)

from app.blueprints.device import device
from flask_login import login_required


@device.route('/', methods=['GET', 'POST'])
@login_required
def devices():
    return render_template('device/devices.html', title="Abrechnung")


@device.route('/<id>/', methods=['GET', 'POST'])
@login_required
def device_view():
    return "under construction"
