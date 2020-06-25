from flask import Flask

# ! Secret key to facilitate encyrption
# ? Pleace a key into the create_app() method into
# * package constructor __init__.py


def create_app():
    # * can we rehash other code in img src now?
    app = Flask(__name__, static_url_path='/wineproj/static')
    app.debug = True

    # * from . import wineproj
    from wineproj import views
    app.register_blueprint(views.bp)

    # app.secret_key='secretkey'  ||  # ? cookie encryption
    return app
