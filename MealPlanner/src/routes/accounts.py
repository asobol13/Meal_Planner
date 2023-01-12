from flask import Blueprint, jsonify, abort, request
from ..models import Account, db
import hashlib
import secrets

# Scramble function here
def scramble(user_key:str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((user_key + salt).encode('utf-8')).hexdigest()

# Creating blueprint
bp = Blueprint('accounts', __name__, url_prefix='/accounts')

# Getting index of the accounts
@bp.route('', methods=['GET'])
def index():
    accounts = Account.query.all()
    result = []
    for a in accounts:
        result.append(a.serialize())
    return jsonify(result)

# Showing specific accounts
@bp.route('/<int:account_id>', methods=['GET'])
def show(account_id:int):
    a = Account.query.get_or_404(account_id)
    return jsonify(a.serialize())

# Creating accounts
@bp.route('', methods=['POST'])
def create():
    # Request body muct contain username and user_key
    if 'username' not in request.json or 'user_key' not in request.json:
        return abort(400)
    if len(request.json['username']) < 3 or len(request.json['user_key']) < 8:
        return abort(400)
    # Construct account
    a = Account(
        username = request.json['username'],
        user_key = request.json['user_key']
    )
    db.session.add(a) # Preparing create statement
    db.session.commit() # Executing create statement
    return jsonify(a.serialize())

# Deleting the accounts
# Deleting accounts
@bp.route('/<int:account_id>', methods = ['DELETE'])
def delete(account_id:int):
    a = Account.query.get_or_404(account_id)
    try:
        db.session.delete(a) # prepare delete statement
        db.session.commit() # execute delete statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)

# Updating the accounts
@bp.route('/<int:account_id>', methods = ['PATCH', 'PUT'])
def update(account_id:int):
    a = Account.query.get_or_404(account_id)
    if (
        'username' not in request.json and
        'user_key' not in request.json):
        return abort(400)

    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        a.username = request.json['username']
    if 'user_key' in request.json:
        if len(request.json['user_key']) < 8:
            return abort(400)
        a.user_key = scramble(request.json['user_key'])

    try:
        db.session.commit()
        return jsonify(a.serialize())
    except:
        return jsonify(False)