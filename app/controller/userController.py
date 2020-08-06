from flask import (
    Blueprint,
    render_template
)

user = Blueprint('user', __name__, url_prefix='/user')

""" blueprint to administrate users """


@user.route('/', methods=['GET', 'POST'])
def users():
    return render_template('user/user.html', title="Benutzer")


@user.route('/<id>/', methods=['GET', 'POST'])
def userview():
    return "under construction"
