from flask import Blueprint

clock_in = Blueprint('clock_in', __name__)

from app.blueprints.clockIn import errors
from app.blueprints.clockIn import (
    clock_in_view
)
