from flask import (
    render_template,
    url_for,
    redirect,
    flash,
)

from app.models.user import User
from app.blueprints.auth import auth
from app.blueprints.auth.forms import LoginForm


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Benutzername oder Passwort falsch', )
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html',
                           title='Login',
                           form=form,
                           )
