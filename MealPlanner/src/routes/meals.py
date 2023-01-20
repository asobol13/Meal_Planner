# from flask import Blueprint, jsonify, abort, request
# from ..models import Meal, db

# # Creating blueprint
# bp = Blueprint('meals', __name__, url_prefix='/meals')

# # Getting random meals
# @bp.route('', methods = ['GET'])
# def cat_beef():
#     return

# def cat_chicken():
#     return

# def cat_seafood():
#     return

# def cat_veggies():
#     return

# def cat_instantpot():
#     return

# def cat_grill():
#     return

# def cat_stove():
#     return

# def cat_oven():
#     return

# def cat_italian():
#     return

# def cat_asian():
#     return

# def cat_mexican():
#     return

# def cat_american():
#     return

# def quick_cooking():
#     return

# # Return a randomized meal
# @bp.route('</int:meal_id>', methods = ['GET'])
# def show(meal_id:int):
#     m = Meal.query.get_or_404(meal_id)
#     return jsonify(m.serialize())

# Eventually:
# Add on a create option for the meals
# On top of creating you can update/ make additions to your created meals?
# You can delete meals