from flask import Blueprint

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return '<h1>Testing blueprint page</h1>'


@bp.route('/secret')
def secret():
    return '<h1>Secondard test for blueprint</h1>'
