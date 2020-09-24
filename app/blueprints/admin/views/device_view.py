from datetime import datetime

from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
)
from app import db
from app.blueprints.admin import admin
from flask_login import login_required, current_user
from app.helper.decorator import manager_required, owner_required
from app.models.device import Device
from app.models.user import User
from app.blueprints.admin.forms.device_forms import DeviceAddForm, DeviceEditForm


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
    form = DeviceEditForm()
    device = Device.query.filter(Device.label == name).first()

    if not current_user.is_owner():
        flash("Unzureichende Rechte")
        return redirect(url_for('admin.devices'))

    if request.method == 'POST':
        if form.validate_on_submit():
            device.label = form.label.data
            device.manufacturer = form.manufacturer.data
            device.ordered_from = form.ordered_from.data
            device.modified_at = datetime.now().strftime('%d %b, %H:%M:%S')
            if Device.query.filter(Device.device_uuid == form.uuid.data).first() is None:
                device.device_uuid = form.uuid.data
            if Device.query.filter(Device.serial_number == form.serial.data).first() is None:
                device.serial_number = form.serial.data
            db.session.commit()
            flash('Gerät erfolgreich geändert')
            return redirect(url_for('admin.devices'))

    form.sn.data = device.serial_number
    form.ud.data = device.device_uuid
    form.label.data = device.label
    form.uuid.data = device.device_uuid
    form.serial.data = device.serial_number
    form.manufacturer.data = device.manufacturer
    form.ordered_from.data = device.ordered_from

    return render_template('admin/device/parts/device-edit.html', name=name, form=form)


@admin.route('/devices/<uuid>/delete', methods=['GET'])
@login_required
@owner_required
def delete_device(uuid):
    if current_user.is_owner() or current_user.is_administrator():
        device = Device.query.filter(Device.device_uuid == uuid).first()
        db.session.delete(device)
        db.session.commit()
        flash('Gerät erfolgreich gelöscht', 'success')
        return redirect(url_for('admin.devices'))
    else:
        flash("Unzureichende Berechtigung", 'error')
        return redirect(url_for('admin.devices'))


@admin.route('/devices/add', methods=['GET', 'POST'])
@login_required
@owner_required
def add_device():
    form = DeviceAddForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            device = Device(
                label=form.label.data,
                device_uuid=form.uuid.data,
                serial_number=form.serial.data,
                manufacturer=form.manufacturer.data,
                ordered_from=form.ordered_from.data,
                created_at=datetime.now().strftime('%d %b, %H:%M:%S'),
                modified_at=datetime.now().strftime('%d %b, %H:%M:%S'),
            )
            db.session.add(device)
            db.session.commit()
            flash('Gerät erfolgreich angelegt', 'success')
            return redirect(url_for('admin.devices'))
    return render_template('admin/device/parts/device-add.html', form=form)
