from flask import render_template, flash, redirect, url_for
from app import app



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
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    return render_template('login.html', title='Sign In')
