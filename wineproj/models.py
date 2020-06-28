# ORM for SQL alchemy
# These are simply our Class definitions from part 1, with string/repr formats

from . import db


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default='reds.jpg')
    wines = db.relationship('Wine', backref='category',
                            cascade="all, delete-orphan")  # ? Type or "vinoType"
    # * tours = db.relationship('Tour', backref='City', cascade="all, delete-orphan") for class

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}\n"
        str = str.format(self.id, self.name, self.description, self.image)
        return str


orderdetails = db.Table('orderdetails',
                        db.Column('order_id', db.Integer, db.ForeignKey(
                            'orders.id'), nullable=False),
                        db.Column('wine_id', db.Integer, db.ForeignKey(
                            'wines.id'), nullable=False),
                        db.PrimaryKeyConstraint('order_id', 'wine_id'))


class Wine(db.Model):
    __tablename__ = 'wines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    blend = db.Column(db.String(50), nullable=False)
    vintage = db.Column(db.String(20), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        str = "ID: {}, Name: {}, Blend: {}, Vintage: {}, Region: {}, Image: {}, Price: {}, Type: {}, Description: {}\n"
        str = str.format(self.id, self.name, self.blend, self.vintage,
                         self.region, self.image, self.price, self.category_id, self.description)
        return str


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    date = db.Column(db.DateTime)
    totalcost = db.Column(db.Float)
    wines = db.relationship("Wine", secondary=orderdetails, backref="orders")
    # tours = db.relationship("Tour", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "ID: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Date: {}, Wines: {}, Total Cost: {}\n"
        str = str.format(self.id, self.status, self.firstname, self.surname,
                         self.email, self.phone, self.date, self.wines, self.totalcost)
        return str


# ! class vinoType(db.Model):
#     def __init__(self, id, name, description, image):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.image = image

#     def get_vinoType_details(self):
#         return str(self)

#     def __repr__(self):
#         str = "Id: {}, Name: {}, Description: {}, Image: {} \n"
#         str = str.format(self.id, self.name, self.description, self.image)
#         return str

# class Vino:
#     def __init__(self, id, name, description, image, price, vinotype, date):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.image = image
#         self.price = price
#         self.vinotype = vinotype        # self.city = city
#         self.date = date

#     def get_vino_details(self):
#         return str(self)

#     def __repr__(self):
#         str = "Id: {}, Name: {}, Description: {}, Image: {}, Price: {}, Type: {}, Date: {}\n"
#         str = str.format(self.id, self.name, self.description,
#                          self.image, self.price, self.vinotype, self.date)
#         return str

# # The order & the Cart can be merged together as one object.  Python OOP.


# class Order:
#     def __init__(self, id, status, firstname, surname, email, phone, date, tours, total_cost):
#         self.id = id
#         self.status = status
#         self.firstname = firstname
#         self.surname = surname
#         self.email = email
#         self.address = address
#         self.date = date
#         self.tours = tours
#         self.total_cost = total_cost        # this is usually calculated

#     def get_order_details(self):
#         return str(self)

#     def __repr__(self):
#         str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Addres: {}, Date: {}, Tours: {}, Total Cost: {}\n"
#         str = str.format(self.id, self.status, self.firstname, self.surname,
#                          self.email, self.address, self.date, self.tours, self.total_cost)
#         return str
