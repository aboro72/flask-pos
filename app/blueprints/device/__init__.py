from flask import Blueprint

device = Blueprint('device', __name__)

from app.blueprints.device import errors, views
