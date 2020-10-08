from flask import (
    render_template,
    request,
    redirect,
    url_for,
)
from flask_login import login_required

from app.blueprints.pos import pos

from app.models.pos import Pos


@pos.route('/', methods=['GET', 'POST'])
@login_required
def cash():
    querys = Pos.query.all()
    unfinished_bills = list()
    for query in querys:
        if query.billed_at is None:
            unfinished_bills.append(query)
    return render_template('pos/pos-index.html',
                           title="Kasse",
                           route=request.path,
                           checkouts=unfinished_bills
                           )


@pos.route('/bill/<pos_id>/', methods=['GET', 'POST'])
@login_required
def bill(pos_id):
    bill = Pos.query.get(pos_id)

    return render_template('pos/parts/pos-bill.html',
                           title="Kasse {} abrechnen".format(bill.control_device_id),
                           route=request.path,
                           billed=bill
                           )

