# ! note the inclusion of the __init__.py file ==> wineproj is a pkg

from wineproj import create_app

if __name__ == "__main__":
    napp = create_app()
    napp.run(debug=True)

    # testing github
# testing again
