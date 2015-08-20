from . import main

from flask import render_template

@main.route('/')
def index():
    return "It's working"

@main.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
