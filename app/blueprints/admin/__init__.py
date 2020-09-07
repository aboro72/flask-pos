from flask import Blueprint

admin = Blueprint('admin', __name__)

from app.blueprints.admin import errors
from app.blueprints.admin.views import (
    users, administrate, control, devices
)
