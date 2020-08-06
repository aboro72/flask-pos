from flask import (
    Blueprint, render_template
)

main = Blueprint('main', __name__, url_prefix='')

""" blueprint for main main """


@main.route('/')
@main.route('/index/')
@main.route('/home/')
def index():
    return render_template('main/index.html', title="Hauptseite")


@main.route('/impressum/')
def impressum():
    return render_template('main/impressum.html', title="Impressum")
