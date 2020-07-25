import logging
from flask import Blueprint, render_template
from . import db


def debug(datei="server.log"):
    logging.basicConfig(filename=datei,format='%(asctime)s %(message)s',  datefmt='%d/%m/%Y %H:%M:%S ', level=logging.INFO)
    logging.error('Error: ')
    logging.critical('Kritischer Fehler!!!!!: ')


debug(datei='app.log')

main = Blueprint('main', __name__)




@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')