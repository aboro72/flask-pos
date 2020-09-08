from flask import (
    render_template,
    flash,
    redirect,
    url_for,
)
from flask_login import login_required, current_user
from app.blueprints.admin import admin


@admin.before_app_request
def before_request():
    if current_user.is_authenticated:
        if not current_user.is_active:
            flash('Benutzer nicht aktiviert', 'WARNING')
            redirect(url_for('main.index'))


@admin.route('/')
@admin.route('/dashboard/')
@login_required
def dashboard():
    return render_template('admin/admin.html', title="Verwaltung")