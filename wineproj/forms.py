# WTForms do a lot of the heavy lifting in validation & CSRF
# Flask-WTF maps form into an object, that can be used in Python OOP
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# FlaskForm represents the form as an Class – better OOP practise


class CheckoutForm(FlaskForm):
    firstname = StringField("Your first name", validators=[InputRequired()])
    surname = StringField("Your surname", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email(
        message="Email is required for your account!")])
    phone = StringField("Your phone", validators=[InputRequired(
        message="A phone number is required for SMS confirmation")])
    address = StringField("Your address", validators=[InputRequired(
        message="An address is required for delivery")])
    submit = SubmitField("Confirm purchase & send order")
