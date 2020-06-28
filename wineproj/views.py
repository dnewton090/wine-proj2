# ! session requires app.secret_key to be set
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from datetime import datetime
from wineproj.forms import CheckoutForm
from wineproj.models import Order, Wine, Category

# Had a huge issue with 2x bp objects – when naming the bp in admin page as well–
bp = Blueprint('main', '__name__')


@bp.route('/')
@bp.route('/index')
def index():
    # categories = Category.query.order_by(Category.name).all()
    # return render_template('index.html', categories=categories)
    return render_template('index.html')


@bp.route('/wines/<int:category>/')
def wines(category):
    wines = Wine.query.filter(Wine.category_id == category)
    return render_template('wines.html', wines=wines)


@bp.route('/checkout', methods=["POST", "GET"])
def checkout():
    return "not implemented yet"
    # form = CheckoutForm()
    # if 'order_id' in session:
    #     order = Order.query.get_or_404(session['order_id'])

    #     if form.validate_on_submit():
    #         order.status = True
    #         order.firstname = form.firstname.data
    #         order.surname = form.surname.data
    #         order.email = form.email.data
    #         order.phone = form.phone.data
    #         totalcost = 0
    #         for wine in order.wines:
    #             totalcost = totalcost + wine.price
    #         order.totalcost = totalcost
    #         order.date = datetime.now()
    #         try:
    #             db.session.commit()
    #             del session['order_id']
    #             flash(
    #                 'Testing, 123')
    #             return redirect(url_for('main.index'))
    #         except:
    #             return 'There was an issue completing your order'

    # return render_template('checkout.html', form=form)


@bp.route('/cart', methods=["POST", "GET"])
def cart():
    # need the request object to be imported (for GET/POST)
    # print statement into the terminal
    print('First name: {}\nLast name: {}\nAddress: {}'
          .format(request.values.get('firstname'), request.values.get('surname'), request.values.get('address')))

    session['firstname'] = request.values.get('firstname')

    return render_template('cart.html')

# Referred to as "Basket" to the user


@bp.route('/order', methods=['POST', 'GET'])
def order():
    return "not implemented yet"
# def order():
#     wine_id = request.values.get('wine_id')

#     # retrieve order if there is one
#     if 'order_id' in session.keys():
#         order = Order.query.get(session['order_id'])
#         # order will be None if order_id stale
#     else:
#         # there is no order
#         order = None

#     # create new order if needed
#     if order is None:
#         order = Order(status=False, firstname='', surname='',
#                       email='', phone='', totalcost=0, date=datetime.now())
#         try:
#             db.session.add(order)
#             db.session.commit()
#             session['order_id'] = order.id
#         except:
#             print('failed at creating a new order')
#             order = None

#     # calcultate totalprice
#     totalprice = 0
#     if order is not None:
#         for tour in order.tours:
#             totalprice = totalprice + tour.price

#     # are we adding an item?
#     if wine_id is not None and order is not None:
#         tour = Wine.query.get(wine_id)
#         if tour not in order.tours:
#             try:
#                 order.tours.append(tour)
#                 db.session.commit()
#             except:
#                 return 'There was an issue adding the item to your basket'
#             return redirect(url_for('main.order'))
#         else:
#             flash('item already in basket')
#             return redirect(url_for('main.order'))

#     return render_template('order.html', order=order, totalprice=totalprice)


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
    return "not implemented yet"
# def deleteorderitem():
#     id = request.form['id']
#     if 'order_id' in session:
#         order = Order.query.get_or_404(session['order_id'])
#         tour_to_delete = Wine.query.get(id)
#         try:
#             order.tours.remove(tour_to_delete)
#             db.session.commit()
#             return redirect(url_for('main.order'))
#         except:
#             return 'Problem deleting item from order'
#     return redirect(url_for('main.order'))


# Scrap basket
@bp.route('/deleteorder')
def deleteorder():
    return "not implemented yet"
# def deleteorder():
#     if 'order_id' in session:
#         del session['order_id']
#         flash('All items deleted')
#     return redirect(url_for('main.index'))
