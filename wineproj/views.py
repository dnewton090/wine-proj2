from flask import Blueprint, render_template, request
from flask import session, redirect, url_for, flash

bp = Blueprint('wineproj', '__name__')

# ? None of the below is working –– although my side is opening up index.html


@bp.route('/')
@bp.route('/index')
@bp.route('/home')
def index():
    # return render_template('index.html')
    return '<h1>Testing blueprint page</h1>'


@bp.route('/index2')
def index2():
    return render_template('index2.html')


@bp.route('/secret')
def secret():
    return '<h1>Test @bp exists</h1>'
