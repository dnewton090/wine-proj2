from flask import Flask, render_template
# Quick & easy way for Flask to interface with forms
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy     # issues importing?

# ! Secret key to facilitate encyrption
# ? Pleace a key into the create_app() method into
# * package constructor __init__.py

app = Flask(__name__, static_url_path='/wineproj/static')


def create_app():
    app.debug = True
    # python import os; os.urandom(12)  # ! session encyption inside cookie
    app.secret_key = 'q\x00\x1c\xb3j?\xe7\x84\x8c\xd7\xb6C'

    # sets the app configuration data
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wineproj.sqlite'

    db.init_app(app)

    bootstrap = Bootstrap(app)

    # * from wineproj import views
    from . import views
    app.register_blueprint(views.bp)

    return app


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html")
