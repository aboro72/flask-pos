from datetime import datetime

from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
)
from flask_login import login_required, current_user

from app import db
from app.helper.decorator import manager_required, owner_required
from app.blueprints.admin import admin
from app.models.user import User
from app.models.role import Role

from app.blueprints.admin.forms.user_forms import UserAddForm, UserEditForm


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


@admin.route('/users/<name>/view/', methods=['GET'])
@login_required
@manager_required
def get_user(name):
    user = User.query.filter(User.username == name).first()
    return render_template('admin/user/parts/user-view.html', user=user)


@admin.route('/users/<name>/edit/', methods=['GET', 'POST'])
@login_required
@owner_required
def edit_user(name):

    form = UserEditForm()
    user = User.query.filter(User.username == name).first()
    form.role.choices = [(r.role_id, r.name) for r in
                         Role.query.filter(Role.permissions <= current_user.role.permissions)]

    if current_user.role.permissions < user.role.permissions:
        flash("Unzureichende Rechte")
        return redirect(url_for('admin.users'))

    if request.method == 'POST':
        print(user)
        user.role = Role.query.get(form.role.data)
        user.email = form.email.data
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        if user.uuid == form.uuid.data or User.query.filter(User.uuid == form.uuid.data).first() is None:
            if user.uuid != form.uuid.data:
                user.uuid = form.uuid.data
            db.session.commit()
            flash('Benutzer erfolgreich geändert')
            return redirect(url_for('admin.users'))
        flash('Die Mitarbeiter-ID ist schon vorhanden')
        return render_template('admin/user/parts/user-edit.html', username=name, form=form, title=name)
        # print("form is not valid")
        # print(user.role)
        # print(user.email)
        # print(user.user_id)
        # print(user.email)
        # print(user.firstname)
        # return redirect(url_for('admin.users'))

    form.role.data = user.role_id
    form.email.data = user.email
    form.firstname.data = user.firstname
    form.lastname.data = user.lastname
    form.uuid.data = user.uuid
    form.ud.data = user.uuid
    form.ve.data = user.email

    return render_template('admin/user/parts/user-edit.html', username=name, form=form, title=name)


@admin.route('/users/<name>/delete/', methods=['GET'])
@login_required
@owner_required
def delete_user(name):
    # delete user
    if current_user.is_owner() or current_user.is_administrator():
        user = User.query.filter(User.username == name).first()
        if current_user.role.permissions > user.role.permissions:
            db.session.delete(user)
            db.session.commit()
            flash('Benutzer erfolgreich gelöscht')
            return redirect(url_for('admin.users'))
        flash("Unzureichende Berechtigung")
        return redirect(url_for('admin.users'))
    flash('Nutzer ist nicht berechtigt')
    return redirect(url_for('admin.users'))


@admin.route('/users/add/', methods=['GET', 'POST', ])
@login_required
@manager_required
def add_user():
    form = UserAddForm()
    form.role.choices = [(r.role_id, r.name) for r in
                         Role.query.filter(Role.permissions <= current_user.role.permissions)]
    if request.method == 'POST':
        if form.validate_on_submit():
            selected = Role.query.get(form.role.data)

            user = User(
                username=form.username.data,
                password='0000',
                email=form.email.data,
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                uuid=form.uuid.data,
                role=selected,
                created_at=datetime.now().strftime('%d %b, %H:%M:%S'),
                modified_at=datetime.now().strftime('%d %b, %H:%M:%S'),
                is_active=False
            )
            db.session.add(user)
            db.session.commit()
            flash('Benutzer erfolgreich angelegt')
            return redirect(url_for('admin.users'))
    form.role.default = 1
    return render_template('admin/user/parts/user-add.html', form=form)
