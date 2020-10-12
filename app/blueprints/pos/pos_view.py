from datetime import datetime

from flask import (
    render_template,
    request,
    redirect,
    url_for,
)
from flask_login import login_required, current_user

from app import db
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
    billed = Pos.query.get(pos_id)
    if request.method == 'POST':
        form_data = request.form.get('abrechnen')
        if form_data is not None:
            billed.total_amount = form_data * 100
            billed.billed_at = datetime.now()
            billed.billed_by = current_user.user_id
            db.session.commit()
            return redirect(url_for('pos.cash'))
    return render_template('pos/parts/pos-bill.html',
                           title="Kasse {} abrechnen".format(billed.control_device_id),
                           route=request.path,
                           billed=billed
                           )
