""" imports """

# standard packages
import datetime
# external packages
from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


# internal packages
from config import config

# declare packages
mail = Mail()
moment = Moment()
db = SQLAlchemy(session_options={"autoflush": False})
#db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()


def create_app(config_name):
    # config app
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.models.pos import Pos
    from app.models.user import User
    from app.models.role import Role
    from app.models.device import Device
    from app.models.message import Message
    from app.models.control import Control

    # blueprints import
    from app.blueprints import (
        pos as pos_controller,
        main as main_controller,
        auth as auth_controller,
        admin as admin_controller,
    )

    # register blueprints
    app.register_blueprint(main_controller.main, url_prefix='')
    app.register_blueprint(auth_controller.auth, url_prefix='/auth')
    app.register_blueprint(admin_controller.admin, url_prefix='/admin')
    app.register_blueprint(pos_controller.pos, url_prefix='/pos')

    return app


