from flask import Blueprint

admin = Blueprint('admin', __name__)

from app.blueprints.admin import errors
from app.blueprints.admin.views import (
    control_view,
    dashboard_view,
    device_view,
    user_view,
    msg_view,
)
