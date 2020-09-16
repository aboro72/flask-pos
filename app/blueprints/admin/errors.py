from flask import (
    render_template
)

from app.blueprints.admin import admin
from flask_wtf.csrf import CSRFError


@admin.app_errorhandler(404)
def page_not_found():
    return render_template('error/404.html'), 404


@admin.app_errorhandler(500)
def internal_server_error():
    return render_template('error/500.html'), 500


@admin.app_errorhandler(CSRFError)
def handle_csrf_error(error):
    return render_template('error/csrf_error.html',title="CSFR Error", reason=error.description), 400
