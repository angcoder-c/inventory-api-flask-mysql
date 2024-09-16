from . import category_bp
from app.models import Category
from app import db
from flask import jsonify, request

# get categories
@category_bp.route('/', methods=['GET'])
def get_categories ():
    categories = Category.query.all()
    return jsonify([Category.to_dict(cat) for cat in categories])

# get category by id
@category_bp.route('/id/<int:id>', methods=['GET'])
def get_category_by_id (id):
    category = Category.query.get_or_404(id)
    return jsonify(Category.to_dict(category=category))

# create a new category
@category_bp.route('/', methods=['POST'])
def create_category ():
    data = request.get_json()
    new_category = Category(
        name = data['name'],
        description = data['description']
    )

    db.session.add(new_category)
    db.session.commit()
    return jsonify(Category.to_dict(category=new_category))
