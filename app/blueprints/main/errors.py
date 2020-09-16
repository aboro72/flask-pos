from flask import render_template
from flask_wtf.csrf import CSRFError

from app.blueprints.main import main


@main.app_errorhandler(404)
def page_not_found():
    return render_template('error/404.html'), 404


@main.app_errorhandler(500)
def internal_server_error():
    return render_template('error/500.html'), 500


@main.app_errorhandler(CSRFError)
def handle_csrf_error(error):
    return render_template('error/csrf_error.html', title="CSFR Error", reason=error.description), 400
