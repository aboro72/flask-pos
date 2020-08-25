from flask import Blueprint

user = Blueprint('user', __name__)

from app.blueprints.user import errors, views
