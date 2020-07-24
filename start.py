import logging
from flask import Flask


def debug():
    logging.basicConfig(filename="server.log",format='%(asctime)s %(message)s',  datefmt='%d/%m/%Y %H:%M:%S ', level=logging.INFO)
    logging.error('Error: ')


debug()

''' Der eigentlich Codeblock ist mit absicht in ein Try gesetzt . Die Funktion debug() sollte eigentlich alle
    fehler  aufzeichnen. Zumindest wenn alles richtig gemacht habe. Dort stehen auch die debug nachrichten von flask
     wenn der debug=True parameter gesetzt ist in der funktion app.run().'''
try:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hallo World"

    if __name__ == '__main__':
        app.run(port=1337, debug=True)


except ZeroDivisionError:
    print('Durch 0 teilen geht nicht!!')

except RuntimeError:
    print("RuntimeError")

except Exception:
    print('Ups, ein noch Unbekanter Fehler')
