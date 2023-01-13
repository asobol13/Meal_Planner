from flask import Blueprint, jsonify, abort, request
from ..models import Meal, db

# Creating blueprint
bp = Blueprint('meals', __name__, url_prefix='/meals')

# Return a randomized meal
@bp.route('', methods = ['GET'])
def show(meal_id:int):
    m = Meal.query.get_or_404(meal_id)
    return jsonify(m.serialize())