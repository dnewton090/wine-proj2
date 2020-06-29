# ! session requires app.secret_key to be set
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from datetime import datetime
from wineproj.forms import CheckoutForm
from wineproj.models import Order, Wine, Category
from . import db

# Had a huge issue with 2x bp objects – when naming the bp in admin page as well–
bp = Blueprint('main', '__name__')


@bp.route('/')
@bp.route('/index')
def index():
    # SQLAlchemy ORM queries
    categories = Category.query.order_by(Category.id).all()
    wines = Wine.query.order_by(Wine.id).all()

    return render_template('index.html', categories=categories, wines=wines)
    # return render_template('index.html')

# * How to display the name corresponding to the filter?  i.e. wines/reds/ (not wines/1/)


@bp.route('/wines/<int:categoryid>/')
def wines(categoryid):
    wines = Wine.query.filter(Wine.category_id == categoryid)
    return render_template('wines.html', wines=wines)

# ! passing the same variable into another bp (wines) causes the BP Association Error
# ? You cannot have the same function name –– how then to overload?

# @bp.route('/wines')
# def all():
#     products = Wine.query.order_by(Wine.id).all()
#     return render_template('wines.html', products=products)


@bp.route('/order', methods=['POST', 'GET'])
def order():
    # This looks inside the name field of the form
    wine_id = request.values.get('wine_id')

    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status=False, firstname='', surname='',
                      email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None

    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for wine in order.wines:
            totalprice = totalprice + wine.price

    # are we adding an item?  Variable in the request (sent by POST)
    if wine_id is not None and order is not None:
        wine = Wine.query.get(wine_id)
        if wine not in order.wines:
            try:
                order.wines.append(wine)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))

    # !! Need to get this up & running
    return render_template('order.html', order=order, totalprice=totalprice)


@bp.route('/cart', methods=["POST", "GET"])
def cart():
    # need the request object to be imported (for GET/POST)
    # print statement into the terminal
    print('First name: {}\nLast name: {}\nAddress: {}'
          .format(request.values.get('firstname'), request.values.get('surname'), request.values.get('address')))

    session['firstname'] = request.values.get('firstname')

    return render_template('cart.html')

# Referred to as "Basket" to the user


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/base')
def base():
    return render_template('base.html')


@bp.route('/detail')
def detail():
    return render_template('detail.html')

# @bp.route('/wines')
# def wines():©
#     return render_template('wines.html')

# Used for testing out the NavBar


@bp.route('/nav')
def nav():
    return render_template('includes/nav.html')


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        wine_to_delete = Wine.query.get(id)
        try:
            order.wines.remove(wine_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))

# Scrap basket


@bp.route('/deleteall')
def deleteall():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=["POST", "GET"])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.address = form.address.data
            totalcost = 0
            for wine in order.wines:
                totalcost = totalcost + wine.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash(
                    'Testing, 123')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'

    return render_template('checkout.html', form=form)
