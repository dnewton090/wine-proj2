# ! session requires app.secret_key to be set
from flask import Blueprint, render_template, url_for, request, session, flash
from datetime import datetime
from .forms import CheckoutForm

# ? Why not use the folder name wineproj?  Results in == functionality
# bp = Blueprint('wineproj','__main__')
bp = Blueprint('wineproj', '__name__')


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/nav')
def nav():
    return render_template('includes/nav.html')


@bp.route('/cart', methods=["POST", "GET"])
def cart():
    # need the request object to be imported (for GET/POST)
    # print statement into the terminal
    print('First name: {}\nLast name: {}\nAddress: {}'
          .format(request.values.get('firstname'), request.values.get('surname'), request.values.get('address')))

    session['firstname'] = request.values.get('firstname')

    return render_template('cart.html')


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/checkout')
form = checkoutForm()


def checkout():
    return render_template('checkout.html', form=form)


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
