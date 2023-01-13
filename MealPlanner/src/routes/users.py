from flask import Blueprint, jsonify, abort, request
from ..models import User, db

# Creating blueprint
bp = Blueprint('users', __name__, url_prefix='/users')

# Getting index of the users
@bp.route('', methods=['GET'])
def index():
    users = User.query.all()
    result = []
    for u in users:
        result.append(u.serialize())
    return jsonify(result)

# Showing specific users
@bp.route('/<int:user_id>', methods = ['GET'])
def show(user_id:int):
    u = User.query.get_or_404(user_id)
    return jsonify(u.serialize())

# Creating users
@bp.route('', methods=['POST'])
def create():
    # Request body must contain name and dietary_restrictions
    if 'name' not in request.json or 'dietary_restrictions' not in request.json:
        return abort(400)
    # Construct user
    u = User(
        name = request.json['name'],
        dietary_restrictions = request.json['dietary_restrictions']
    )
    db.session.add(u) # Preparing create statement
    db.session.commit() # Executing create statement
    return jsonify(u.serialize())

# Updating the users
@bp.route('/<int:user_id>', methods = ['PATCH', 'PUT'])
def update(user_id:int):
    u = User.query.get_or_404(user_id)
    if (
        'name' not in request.json and
        'dietary_restrictions' not in request.json):
        return abort(400)

    if 'name' in request.json:
        u.name = request.json['name']
    if 'dietary_restrictions' in request.json:
        u.dietary_restrictions = request.json['dietary_restrictions']

    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)
