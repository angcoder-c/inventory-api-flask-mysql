from . import category_bp
from app.models import Category
from flask import jsonify

# get categories
@category_bp.route('/', methods=['GET'])
def get_categories ():
    categories = Category.query.all()
    return jsonify([cat.to_dict() for cat in categories])

# get category by id
@category_bp.route('/<int id>', methods=['GET'])
def get_category_by_id (id):
    category = Category.query.get_or_404(id)
    return jsonify(category.to_dict())

# create a new category
@category_bp.route('/<int id>', methods=['GET'])
def get_category_by_id (id):
    category = Category.query.get_or_404(id)
    return jsonify(category.to_dict())

