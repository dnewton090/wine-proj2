from flask import Flask

# ! Secret key to facilitate encyrption
# ? Pleace a key into the create_app() method into 
# * package constructor __init__.py

def create_app():
    app=Flask(__name__)
    app.debug=True

    # adding a Blueprint (which is:  )
    # Allows you to define views in separate file, and register them @ app initialization
    # All views will be found in the views.py file (which creates .bp)
    from . import views
    app.register_blueprint(views.bp)        ## bp = blueprint?

    # Addition of a secret key for encryption
    # app.secret_key='secretkey'

    return app