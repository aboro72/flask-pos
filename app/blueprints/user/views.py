from flask import (
    render_template,
    flash,
    redirect,
    url_for,
)
from flask_login import login_required, current_user
from app.blueprints.user import user


@user.before_app_request
def before_request():
    if current_user.is_authenticated:
        if not current_user.is_active:
            flash('Sie sind nicht bestätigt', 'WARNING')
            redirect(url_for('main.index'))


@user.route('/', methods=['GET', 'POST'])
@login_required
def users():
    return render_template('user/user.html', title="Benutzer")


@user.route('/<id>/', methods=['GET', 'POST'])
@login_required
def userview():
    return "under construction"
