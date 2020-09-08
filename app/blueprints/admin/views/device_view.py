from flask import (
    render_template,
    flash,
    redirect,
    url_for,
)
from app.blueprints.admin import admin

from flask_login import login_required

from app.helper.decorator import manager_required, owner_required
from app.models.device import Device


@admin.route('/devices/', methods=['GET', 'POST'])
@login_required
@manager_required
def devices():
    devices_list = Device.query.all()
    return render_template('admin/device/device-index.html', title="Abrechnung", devices=devices_list)


@admin.route('/devices/<name>/view', methods=['GET'])
@login_required
@manager_required
def get_device(name):
    device = Device.query.filter(Device.label == name).first()
    return render_template('admin/device/parts/device-view.html', device=device)


@admin.route('/devices/<name>/edit', methods=['GET', 'POST'])
@login_required
@owner_required
def edit_device(name):
    flash("Noch nicht Implementiert")
    # return render_template('admin/device/parts/device-edit.html', device=device)
    return redirect(url_for('admin.devices'))


@admin.route('/devices/<name>/delete', methods=['GET'])
@login_required
@owner_required
def delete_device(name):
    flash("Noch nicht Implementiert")
    return redirect(url_for('admin.devices'))


@admin.route('/devices/add', methods=['GET', 'POST'])
@login_required
@owner_required
def add_device():
    flash("Noch nicht Implementiert")
    return redirect(url_for('admin.devices'))
