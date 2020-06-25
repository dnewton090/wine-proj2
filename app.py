# ! note the inclusion of the __init__.py file ==> wineproj is a pkg

from wineproj import create_app

if __name__ == "__main__":
    napp = create_app()
    napp.run()

    # napp.run(debug=True)
    # ! flask run still opens in Debug: off
    # ? (debug=True) param => Fn as ENV variable below
