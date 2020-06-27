# ORM for SQL alchemy
# These are simply our Class definitions from part 1, with string/repr formats

from datetime import datetime
from . import db

# class City


class vinoType:
    def __init__(self, id, name, description, image):
        self.id = id
        self.name = name
        self.description = description
        self.image = image

    def get_vinoType_details(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {} \n"
        str = str.format(self.id, self.name, self.description, self.image)
        return str


class Vino:
    def __init__(self, id, name, description, image, price, vinotype, date):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.vinotype = vinotype        # self.city = city
        self.date = date

    def get_vino_details(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Price: {}, Type: {}, Date: {}\n"
        str = str.format(self.id, self.name, self.description,
                         self.image, self.price, self.vinotype, self.date)
        return str

# The order & the Cart can be merged together as one object.  Python OOP.


class Order:
    def __init__(self, id, status, firstname, surname, email, phone, date, tours, total_cost):
        self.id = id
        self.status = status
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.address = address
        self.date = date
        self.tours = tours
        self.total_cost = total_cost        # this is usually calculated

    def get_order_details(self):
        return str(self)

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Addres: {}, Date: {}, Tours: {}, Total Cost: {}\n"
        str = str.format(self.id, self.status, self.firstname, self.surname,
                         self.email, self.address, self.date, self.tours, self.total_cost)
        return str
