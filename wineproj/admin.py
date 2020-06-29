'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from wineproj.models import Category, Wine, Order
import datetime

bp = Blueprint('admin', __name__, url_prefix='/admin')

# function to put some seed wines data in the database


@bp.route('/dbseed/')
def dbseed():
    category1 = Category(name="Reds", image="wine_red.jpg", description='''Red wine is a type of wine made from dark-colored grape varieties, and its category includes many of the prized drops in the South East. The actual color of the wine can range from intense violet, typical of young wines, through to brick red for mature wines and brown for older red wines. Common types found in the South East include Cabernet Sauvignon, Shiraz, Grenache, Merlot and Pino Noir.''')
    category2 = Category(name="Whites", image="wine_white.jpg", description='''The wide variety of white wines comes from the large number of varieties, methods of winemaking, and ratios of residual sugar. White wine is mainly from "white" grapes, which are green or yellow in colour, such as Chardonnay, Sauvignon blanc, and Riesling. ''')
    category3 = Category(name="Rose", image="wine_rose.jpg", description='''There are three major ways to produce rosé wine: skin contact, saignée, and blending. Rosé wines can be made still, semi-sparkling or sparkling and with a wide range of sweetness levels from highly dry Provençal rosé to sweet White Zinfandels and blushes. The beauty of a rosé blend is that they can be formulated from awide variety of grapes and can be found all around the globe. ''')
    category4 = Category(name="Fortifieds", image="wine_ports.jpg", description='''Fortified wine is a wine to which a distilled spirit (usually brandy) has been added. Over time winemakers have developed many different styles of fortified wine, including port, sherry, madeira, Marsala, Commandaria wine, and the aromatised wine vermouth. SE Wines speciality is Port wine which is a strong, sweet dark red complex originating from Portugal. It is typically drunk as a dessert wine. ''')
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.add(category4)
        db.session.commit()
    except:
        return "There was an issue adding the wine categories via DBseed"

    # Insert Reds
    w1 = Wine(category_id=category1.id, blend="Cabernet Sauvignon", name="The Surveyor", vintage="2012", region="Coonawarra, SA", image='red_cs_surveyor.png',
              price='69.00', description='A perfect spicy companion, expressing the subtlety of shiraz in a region defined by cool climate and outstanding soil.')
    w2 = Wine(category_id=category1.id, blend="Cabernet Sauvignon", name="The General", vintage="2013", region="Coonawarra, SA", image='red_shiraz_whatso.png', price='28.50',
              description='Waste not, want not. This drop embodies all forms of the bold & the beautiful. Hand plunged, and basket pressed, this is a trial batch Shiraz that is let loose, to be enjoyed with cheese & crackers')
    w3 = Wine(category_id=category1.id, blend="Shiraz", name="The Dark Horse", vintage="2014", region="Coonawarra, SA", image='red_shiraz_darkhorse.png', price='39.50',
              description='Robust aromas of dark and brooding cherries, hints of vanilla with notes from the spice pantry. This shiraz has a broad palate with smooth elegant tannins.')
    w4 = Wine(category_id=category1.id, blend="Merlot", name="The Sailor", vintage="2018", region="Coonawarra, SA", image='red_merlot_more.png', price='29.00',
              description='The cross-blend technique gives this wine grand structure with rich fruits of the forest and a harmonious tannin fingerprint. Merlot encourages softness and juiciness with bursts of ripe blueberries and fresh plum jam.')
    w5 = Wine(category_id=category1.id, blend="Shiraz", name="The Skipper", vintage="2015", region="Penola, SA", image='red_pinot_mc.png', price='99.00',
              description='Foot-crushed shiraz, naturally fermented with no additions, basket pressed, bottled by gravity, hand-labelled, cork-sealed and wax-dipped. Lovely perfumed shiraz with snappy purple berries and a dusting of powdery tannin..')

    # Insert Whites
    w6 = Wine(category_id=category2.id, blend="Viognier", name="VI", vintage="2017", region="Robe, SA", image='white_viognier.png', price='99.00',
              description="Gently basket-pressed to a two-year-old French Oak barrel, this complex wine displays lemon, peach iced tea, spice, grip and texture, with balanced natural acidity and fruit sweetness.")
    w7 = Wine(category_id=category2.id, blend="Chardonnary", name="The Yearling", vintage="2018", region="Padthaway, SA", image='white_char_yearling.png', price='18.00',
              description="Fresh from the Rymill Coonawarra stable, The Yearling is a racy Coonawarra Chardonnay. Made from estate-grown fruit, this crisp and appealing wine is perfect for enjoying now.")
    w8 = Wine(category_id=category2.id, blend="Rielsling", name="gt dry", vintage="2019", region="McLaren Vale, SA", image='white_ries_gt.png', price='22.50',
              description="A delicate and beautifully textured wine made to match a variety of foods, showing the complexity of perfumed aromas and flavours.")

    # Insert Rosé
    w9 = Wine(category_id=category3.id, blend="Rosé", name="Yearling Whooshka", vintage="2019", region="Clare, SA", image='rose_yearling.png', price='16.75',
              description="The Yearling Rosé is a delight to the senses. A real cocktail of summer fruits with a balanced palate and a refreshing finish.")
    w10 = Wine(category_id=category3.id, blend="Rosé", name="Petit Verdot", vintage="2017", region="Nuriootpa, SA", image='rose_petitverdot.png', price='31.00',
               description="This single release Petit Verdot smells like gentle waves of pretty violet and potpourri. It’s gorgeous, bright, juicy, seductive, and all class. ")

    # Insert Ports
    w11 = Wine(category_id=category4.id, blend="Port", name="Galway Pipe", vintage="2010", region="Kalangadoo, SA", image='port_galway.png', price='31.00',
               description='Port lovers have known about the quality of Galway Pipe for decades and with an average age of twelve years that gives this iconic tawny luscious flavours of fruitcake and raisin, its balanced nicely by nutty rancio characteristics.')
    w12 = Wine(category_id=category4.id, blend="Port", name="Penfolds", vintage="2012", region="Dry Creek, SA", image='port_penfolds.png', price='33.00',
               description='A blend of many outstanding tawny components separately matured in seasoned old oak casks, with a minimum blended average age of ten years. The results yields a wine of generous concentration, vitality, exceptional balance of fruit and oak age complexity. The tawny lingers in the mouth, finishing clean and tight.')

    try:
        db.session.add(w1)
        db.session.add(w2)
        db.session.add(w3)
        db.session.add(w4)
        db.session.add(w5)
        db.session.add(w6)
        db.session.add(w7)
        db.session.add(w8)
        db.session.add(w9)
        db.session.add(w10)
        db.session.add(w11)
        db.session.add(w12)
        db.session.commit()
    except:
        return "There was an issue adding a wine in dbseed function"

    return "DATA LOADED"

    # class Wine(db.Model):
    # __tablename__='wines'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50), nullable=False)
    # blend = db.Column(db.String(50), nullable=False)
    # vintage = db.Column(db.String(20),nullable=False)
    # region = db.Column(db.String(50), nullable=False)
    # image = db.Column(db.String(50), nullable=False)
    # price = db.Column(db.Float, nullable=False)
    # description = db.Column(db.String(200), nullable=False)
    # category_id = db.Column(db.Integer, db.ForeignKey('categoriess.id'))
