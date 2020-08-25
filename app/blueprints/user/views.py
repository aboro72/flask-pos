from flask import (
    render_template
)
from flask_login import login_required

from app.blueprints.user import user


@user.route('/', methods=['GET', 'POST'])
@login_required
def users():
    return render_template('user/user.html', title="Benutzer")


@user.route('/<id>/', methods=['GET', 'POST'])
@login_required
def userview():
    return "under construction"
