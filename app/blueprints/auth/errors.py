from flask import (
    render_template,
    request,
)
from flask_wtf.csrf import CSRFError

from app.blueprints.auth import auth


@auth.app_errorhandler(404)
def page_not_found():
    return render_template('error/404.html',
                           title="Seite nicht gefunden",
                           route=request.path
                           ), 404


@auth.app_errorhandler(500)
def internal_server_error():
    return render_template('error/500.html',
                           title="Interner Fehler",
                           route=request.path
                           ), 500


@auth.app_errorhandler(CSRFError)
def handle_csrf_error(error):
    return render_template('error/csrf_error.html',
                           title="CSFR Error",
                           reason=error.description,
                           route=request.path
                           ), 400
