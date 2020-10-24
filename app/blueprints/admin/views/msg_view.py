from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
)
from flask_login import login_required, current_user
from app.helper.decorator import owner_required
from app.blueprints.admin import admin
from app.models.message import NewsMessage, SystemNotification


@admin.before_app_request
def before_request():
    if current_user.is_authenticated:
        if not current_user.is_active:
            flash('Benutzer nicht aktiviert', 'warning')
            redirect(url_for('main.index'))


@admin.route('/messages/', methods=['GET', 'POST'])
@login_required
@owner_required
def message_index():
    page = request.args.get('page', 1, type=int)
    message_list = NewsMessage.query.all()
    system_notification = SystemNotification.query.all()
    return render_template('admin/message/message-index.html',
                           title='Benachrichtigungen',
                           sysmessages=True,
                           messages=message_list,
                           notes=system_notification,
                           route=request.path)
