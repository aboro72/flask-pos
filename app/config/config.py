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
        'sqlite:///data.sqlite'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email
    MAIL_SERVER = 'mail.gmx.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class ProductionConfig(Config):
    # production server
    pass


class DevelopmentConfig(Config):
    # debug messages
    DEBUG = True

    # DB_SERVER = 'localhost'

    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///data-dev.sqlite'

    # FOLDER = "/home/ae4life/tutorial/flask"


class TestingConfig(Config):
    # test messages
    TESTING = True

    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///data-test.sqlite'

