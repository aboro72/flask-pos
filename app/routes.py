from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import PostForm, LoginForm


@app.route('/')
@app.route('/index')
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


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
