from flask import (
    Blueprint,
    render_template
)

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login/')
def login():
    return render_template('auth/login.html', title='Login',)