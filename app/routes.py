from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import PostForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Andreas'}
    posts = [
        {
            'author': {'username': 'Tristan'},
            'body': 'Gail , login ist kaputt'
        },
        {
            'author': {'username': 'Du'},
            'body': 'Ha Haaa, ei weiß !!'
        },
        {
            'author':{'username': 'Mathias'},
            'body':'Eh, soll das jetzt eine POS oder ein CMS werden'
        },
        {
            'author': {'username': 'Du'},
            'body': 'Ich habe da echt kein Plan.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/post')
def post():
    form = PostForm()
    return render_template('tinydemo.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))