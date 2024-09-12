from flask import Blueprint

category_bp = Blueprint('category', __name__, url_defaults='/api/category/')

from . import routes