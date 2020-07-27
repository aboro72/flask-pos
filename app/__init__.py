import logging
from flask import Flask
from flask_tinymce import Tinymce
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


logging.basicConfig(filename='app.log', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S ', level=logging.INFO)
logging.debug('Debug: ')
logging.warning('Warnungen: ')


# -- Init FLASK & Config ---
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
# if app.config["ENV"] == "production":
#    app.config.from_object("config.ProductionConfig")
# elif app.config["ENV"] == "testing":
#    app.config.from_object("config.TestingConfig")
# else:
#    app.config.from_object("config.DevelopmentConfig")


from app import routes



