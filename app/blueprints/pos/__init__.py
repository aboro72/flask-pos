from flask import Blueprint

pos = Blueprint('pos', __name__)

from app.blueprints.pos import errors, views
