from flask import (
    render_template
)

from app.blueprints.admin import admin


@admin.app_errorhandler(404)
def page_not_found():
    return render_template('error/404.html'), 404


@admin.app_errorhandler(500)
def internal_server_error():
    return render_template('error/500.html'), 500
