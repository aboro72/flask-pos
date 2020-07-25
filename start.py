from flask import Flask
from time import asctime
import app   # Hier bitte weitere Funktionen und classen eintragen sonst wird es hier unübersichtlich


app.debug(datei="test.log")


try:
    app = Flask(__name__)


    @app.route('/')
    def index():
        return asctime()  # Hier übergeben wir später an eine index.html oder was auch immer


    if __name__ == '__main__':
        app.run(port=1337, debug=True)


except ZeroDivisionError:
    print('Durch 0 teilen geht nicht!!')

except RuntimeError:
    print("RuntimeError")

except Exception:
    print('Ups, ein noch Unbekanter Fehler')

