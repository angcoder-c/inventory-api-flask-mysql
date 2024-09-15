from flask import Blueprint

category_bp = Blueprint('category', __name__, url_prefix='/api/category/')

from . import routes