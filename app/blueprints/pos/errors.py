from flask import render_template
from app.blueprints.pos import pos


@pos.app_errorhandler(404)
def page_not_found():
    return render_template('error/404.html'), 404


@pos.app_errorhandler(500)
def internal_server_error():
    return render_template('error/500.html'), 500