from flask import Flask, render_template
# Quick & easy way for Flask to interface with forms
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy     # issues importing?

db = SQLAlchemy()
app = Flask(__name__, static_url_path='/wineproj/static')
# app = Flask(__name__)


def create_app():
    app.debug = True
    app.secret_key = 'hexadecimalwarrior'
    # python import os; os.urandom(12)  # ! session encyption inside cookie

    # sets the app configuration data
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wineproj.sqlite'

    # initialize db with flask app
    db.init_app(app)

    # * Changed this to avoid naming conflicts (Assertion Errors)
    bootstrap2 = Bootstrap(app)

    # importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)

    # ! commented out the ADMIN blupeint after loading
    # from . import admin
    # app.register_blueprint(admin.bp)

    return app


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html")
