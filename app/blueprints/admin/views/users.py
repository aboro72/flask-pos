from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
)
from flask_login import login_required, current_user

from app.decorator import manager_required, owner_required
from app.blueprints.admin import admin
from app.models.user import User


@admin.before_app_request
def before_request():
    if current_user.is_authenticated:
        if not current_user.is_active:
            flash('Benutzer nicht aktiviert', 'WARNING')
            redirect(url_for('auth.create_password'))


@admin.route('/users/', methods=['GET', ])
@login_required
@manager_required
def users():
    user_list = User.query.all()
    return render_template('admin/user/user-index.html', title="Benutzer", users=user_list)


@admin.route('/users/<name>/', methods=['GET'])
@login_required
@manager_required
def view_user(name):
    flash('Funktion noch nicht implementiert')
    return redirect(url_for('admin.users'))


@admin.route('/users/<name>/edit', methods=['GET', 'PUT'])
@login_required
@owner_required
def edit_user(name):
    if request.method == 'PUT':
        pass
    else:
        flash('Funktion noch nicht implementiert')
        return redirect(url_for('admin.users'))


@admin.route('/users/<name>/delete', methods=['GET'])
@login_required
@owner_required
def delete_user(name):
    # delete user
    flash('Funktion noch nicht implementiert')
    return redirect(url_for('admin.users'))


@admin.route('/users/add/', methods=['GET', 'POST', ])
@login_required
@manager_required
def add_user():
    flash('Funktion noch nicht implementiert')
    return redirect(url_for('admin.users'))
