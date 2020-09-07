from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

from app.models.role import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                flash('Du hast keine Berechtigung für diese Seite')
                return redirect(url_for('main.index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def user_required(f):
    return permission_required(Permission.USER)(f)


def manager_required(f):
    return permission_required(Permission.MANAGER)(f)


def admin_required(f):
    return permission_required(Permission.ADMIN)(f)


def owner_required(f):
    return permission_required(Permission.OWNER)(f)
