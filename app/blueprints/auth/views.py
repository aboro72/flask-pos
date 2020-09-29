from flask import (
    render_template,
    url_for,
    redirect,
    flash,
    request
)

from flask_login import login_user, logout_user

from app.models.user import User
from app.blueprints.auth import auth
from app.blueprints.auth.forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
                flash('Erfolgreich eingeloggt', 'success')
            return redirect(next)
        flash('Benutzername oder Passwort falsch', 'error')
    return render_template('auth/login.html',
                           title='Login',
                           form=form,
                           route=request.path
                           )


@auth.route('/logout/')
def logout():
    logout_user()
    flash('Erfolgreich ausgeloggt', 'success')
    return redirect(url_for('main.index'))


def create_password():
    flash ('Funktion noch nicht Implementiert')
    return
