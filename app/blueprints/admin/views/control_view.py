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


@admin.route('/control/', methods=['GET', 'POST'])
@login_required
@manager_required
def control():
    control_list = Device.query.all()
    # return render_template('admin/control/control-index.html', title="Abrechnung", controls=control_list)
    flash("Funktion noch nicht implementiert")
    redirect(url_for('admin.dashboard'))
