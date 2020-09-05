from flask import (
    render_template
)
from app.blueprints.admin import admin

from flask_login import login_required

from app.decorator import admin_required


@admin.route('/devices/', methods=['GET', 'POST'])
@login_required
@admin_required
def devices():
    return render_template('admin/device/devices.html', title="Abrechnung")


@admin.route('/devices/<id>/', methods=['GET'])
@login_required
def get_device():
    return "under construction"
