from flask import (
    render_template,
)
from flask_login import login_required

from app.blueprints.admin import admin
from app.decorator import admin_required, manager_required


@admin.route('/controls/', methods=['GET', ])
@login_required
@manager_required
def control():
    return render_template('admin/control/control.html', title="Zeiterfassung")


@admin.route('/control/<id>/', methods=['GET', 'POST'])
@login_required
@manager_required
def control_view():
    return "under construction"


@admin.route('/control/<id>/', methods=['PUT', 'DELETE'])
@login_required
@admin_required
def control_change():
    return "under construction"
