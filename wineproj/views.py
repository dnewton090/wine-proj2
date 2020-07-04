# ! session requires app.secret_key to be set
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from datetime import datetime
from .forms import CheckoutForm
from .models import Order, Wine, Category
from flask_wtf import FlaskForm
from . import db

# Had a huge issue with 2x bp objects – when naming the bp in admin page as well–
bp = Blueprint('main', '__name__')


@bp.route('/')
@bp.route('/index')
def index():
    # SQLAlchemy ORM queries
    wines = Wine.query.order_by(Wine.id).all()
    categories = Category.query.order_by(Category.id).all()
    return render_template('index.html', categories=categories, wines=wines)
    # return render_template('index.html')


@bp.route('/winecategory/<int:categoryid>/')
def wines(categoryid):
    wines = Wine.query.filter(Wine.category_id == categoryid)
    return render_template('wines.html', wines=wines)


@bp.route('/detail/<int:id>/')
def wines2(id):
    wines2 = Wine.query.filter(Wine.id == id)
    return render_template('wines2.html', wines2=wines2)

# ! passing the same variable into another bp (wines) causes the BP Association Error
# ? You cannot have the same function name –– how then to overload?


@bp.route('/order', methods=['POST', 'GET'])
def order():
    # This looks inside the name field of the form
    wine_id = request.values.get('wine_id')
    # retrieve order if there is one
    if 'order_id' in session.keys():
        # * order variable passed into render_template
        order = Order.query.get(session['order_id'])
    else:
        # * order will be None if order_id stale
        order = None

    # create new order -- logically follows on from above
    if order is None:
        order = Order(status=False, totalcost=0, date=datetime.now())
        # order = Order(status=False, firstname='', surname='',
        #               email='', address='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()                 # to update SQLite
            # For order to persist between Requests...Users see total basket
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None

    # * This performs a new calculation every time the basket is displayed
    totalprice = 0
    if order is not None:
        for wine in order.wines:
            # ! This is where we would add Quantity as an extension
            totalprice = totalprice + wine.price

    # are we adding an item?  Variable in the request (sent by POST)
    if wine_id is not None and order is not None:
        wine = Wine.query.get(wine_id)
        if wine not in order.wines:
            try:
                order.wines.append(wine)
                db.session.commit()
            except:
                # For errors in the database
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('This bottle is already in basket. C\'mon, mix it up a little!')
            return redirect(url_for('main.order'))

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

# For testing


@bp.route('/base')
def base():
    return render_template('base.html')


@bp.route('/nav')
def nav():
    return render_template('includes/nav.html')


# Delete specific basket items
# methodS=POST in flask,method=POST in HTML
@bp.route('/deleteorderitem', methods=['POST', 'GET'])
def deleteorderitem():
    id = request.values.get("id")
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        wine_to_delete = Wine.query.get(id)
        try:
            order.wines.remove(wine_to_delete)
            db.session.commit()
            # flash(Wine.query.get(name) + 'deleted from your basket')
            return redirect(url_for('main.order'))
        except:
            return 'Orders must be deleted from the Cart'
    return redirect(url_for('main.order'))

# Deleting the basket & sessionID


@bp.route('/deleteall')
def deleteall():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))

# Causing all of the grief


@bp.route('/checkout', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.address = form.address.data
            totalcost = 0
            for wine in order.wines:
                totalcost = totalcost + wine.price
            order.totalcost = totalcost
            order.date = datetime.now()
            print('First name: {}\nLast name: {}\nEmail: {}\nAddress: {}'
                  .format(request.form.get('firstname'), request.form.get('surname'), request.form.get('phone'),
                          request.form.get('address'), request.form.get('email')))
            try:
                db.session.commit()
                flash("Great job – you're once step closer to a Sunday session!!")
                del session['order_id']
                return redirect(url_for('main.index'))

            except:
                return 'There was an issue completing your order'
    else:
        print('There is nothing in the cart')  # console.log
    return render_template('checkout.html', form=form)
