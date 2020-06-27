# WTForms do a lot of the heavy lifting in validation & CSRF
# Flask-WTF maps form into an object, that can be used in Python OOP

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired, email

# FlaskForm represents the form as an Object – better OOP practise


class CheckoutForm(FlaskForm):
    firstname = StringField("Your first name", validators=[InputRequired()])
    surname = StringField("Your surname", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    address = StringField("Your address", validators=[InputRequired()])
    submit = SubmitField("Confirm purchase & send order")
