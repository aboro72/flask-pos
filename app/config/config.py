""" imports """
import os


class Config(object):
    """ Config file

    This Config file is for different purposes:

        production
        testing
        development

    Switch the configuration by setting the 'FLASK_ENV'
    """

    # the secret key to encode the requests
    SECRET_KEY = \
        os.environ.get('SECRET_KEY') or \
        'this-really-needs-to-be-changed'

    # only sent session-cookie if https is used
    SESSION_COOKIE_SECURE = True

    # staging server
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DATABASE_URL') or \
        'sqlite:///flask-pos.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    # production server
    pass


class DevelopmentConfig(Config):
    # debug messages
    DEBUG = True

    # DB_SERVER = 'localhost'

    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DATABASE_URL') or \
        'sqlite:///flask-pos.db'

    # FOLDER = "/home/ae4life/tutorial/flask"


class TestingConfig(Config):
    # test messages
    TESTING = True

    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DATABASE_URL') or \
        'sqlite:///flask-pos.db'

