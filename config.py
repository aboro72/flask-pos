import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    
    # no debug messages
    DEBUG = False
    
    # no test messages
    TESTING = False
    
    # SECRET_KEY = "\x88|\x0c\x19q\xa5\\(\x8d9\x82!/\xfc\xa4\x8d\xdbe\xc7\x9a\x04s\x04\xe0"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # only sent session-cookie if https is used
    SESSION_COOKIE_SECURE = True
    
    # staging server
    DB_SERVER = '192.168.1.100'  # example ip

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # if we need a upload folder
    # UPLOAD_FOLDER = "/home/gameManager/flask-pos/app/files/upload"
    # POSSIBLE_EXTENSIONS = set(['txt', 'jpg', 'png'])
    

class ProductionConfig(Config):

    # production server
    DB_SERVER = '192.168.1.200'  # example ip


class DevelopmentConfig(Config):
    
    # debug messages
    DEBUG = True

    # DB_SERVER = 'localhost'

    # sqlite for test database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    # FOLDER = "/home/ae4life/tutorial/flask"'sqlite:///' + os.path.join(basedir, 'app.db')

    
class TestingConfig(Config):
    
    # test messages
    TESTING = True

    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
