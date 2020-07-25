import flask_login
from flask import Flask
from time import asctime

from project import app

login_manager = flask_login.LoginManager()


app.debug(datei="test.log")

try:
    app = Flask(__name__)
    login_manager.init_app(app)

    @app.route('/')
    def index():
        return asctime()  # Hier übergeben wir später an eine index.html oder was auch immer


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        pass


    if __name__ == '__main__':
        app.run(port=1337, debug=True)


except ZeroDivisionError:
    print('Durch 0 teilen geht nicht!!')

except RuntimeError:
    print("RuntimeError")

except Exception:
    print('Ups, ein noch Unbekanter Fehler')
