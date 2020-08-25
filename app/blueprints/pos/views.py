from flask import (
    render_template,
)

from app.blueprints.pos import pos


@pos.route('/', methods=['GET', 'POST'])
def cash():
    return render_template('pos/pos.html', title="Abrechnung")


@pos.route('/<id>/', methods=['GET', 'POST'])
def pos_view():
    return "under construction"
