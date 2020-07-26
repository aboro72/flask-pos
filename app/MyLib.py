import logging
from flask import Flask, url_for, render_template

app = Flask(__name__)


logging.basicConfig(filename='app.log', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S ', level=logging.INFO)
logging.debug('Debug: ')
logging.warning('Warnungen: ')


# View
def first():
    @app.route('/')
    def index():
        return render_template('index.html')
