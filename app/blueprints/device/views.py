from flask import (
    render_template
)

from app.blueprints.device import device


@device.route('/', methods=['GET', 'POST'])
def devices():
    return render_template('device/devices.html', title="Abrechnung")


@device.route('/<id>/', methods=['GET', 'POST'])
def device_view():
    return "under construction"
