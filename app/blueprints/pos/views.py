from flask import (
    render_template,
    request
)
from flask_login import login_required

from app.blueprints.pos import pos


@pos.route('/', methods=['GET', 'POST'])
@login_required
def cash():
    return render_template('pos/pos.html',
                           title="Kasse",
                           route=request.path
                           )
