from flask import (
    render_template
)

from app.blueprints.user import user


@user.route('/', methods=['GET', 'POST'])
def users():
    return render_template('user/user.html', title="Benutzer")


@user.route('/<id>/', methods=['GET', 'POST'])
def userview():
    return "under construction"
