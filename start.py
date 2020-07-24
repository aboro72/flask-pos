import logging
from flask import Flask


def debug():
    logging.basicConfig(filename="server.log",format='%(asctime)s %(message)s',  datefmt='%d/%m/%Y %H:%M:%S ', level=logging.INFO)
    logging.error('Error: ')


debug()


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
