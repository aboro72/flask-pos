from flask import Blueprint

control = Blueprint('control', __name__)

from app.blueprints.control import errors, views
