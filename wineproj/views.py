from flask import Blueprint, render_template, request
from flask import session, url_for, flash, redirect

# ? Why not use the folder name wineproj?  Results in == functionality
# bp = Blueprint('wineproj','__main__')
bp = Blueprint('wineproj', '__name__')


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/cart')
def cart():
    ####

    return render_template('cart.html')


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/base')
def base():
    return render_template('base.html')


@bp.route('/detail')
def detail():
    return render_template('detail.html')


@bp.route('/products')
def products():
    return render_template('products.html')


@bp.route('/index2')
def extendbase():
    return render_template('index2.html')


@bp.route('/secret')
def secret():
    return '<h1>Test @bp exists</h1>'
