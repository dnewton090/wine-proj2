from flask import Flask

# ! Secret key to facilitate encyrption
# ? Pleace a key into the create_app() method into
# * package constructor __init__.py


def create_app():
    app = Flask(__name__)
    app.debug = True

    # from . import wineproj
    from . import views
    app.register_blueprint(views.bp)

    # app.secret_key='secretkey'  ||  # ? encryption for cookies
    return app
