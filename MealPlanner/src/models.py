from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Setting up the class for accounts table
class Account(db.Model):
    __tablename__= 'accounts'
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    user_key = db.Column(db.String(255), nullable=False)

    # Initializing the accounts table
    def __init__(self, username:str, user_key:str):
        self.username = username
        self.user_key = user_key

    # Returning accounts table into json
    def serialize(self):
        return {
            'account_id': self.account_id,
            'username': self.username,
            'user_key': self.user_key
        }

# Setting up the class for users table
class User(db.Model):
    __tablename__='users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    dietary_restrictions = db.Column(db.Boolean, nullable=True, default=False)

    # Initializing the users table
    def __init__(self, name:str, dietary_restrictions:bool):
        self.name = name
        self.dietary_restrictions = dietary_restrictions

    # Returning accounts table into json
    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'dietary_restrictions': self.dietary_restrictions
        }

#Setting up the class for meals table
class Meal(db.Model):
    __tablename__='meals'
    meal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meal_name = db.Column(db.String(255), nullable=False)
    recipes = db.Column(db.String(255), nullable = False)
    ingredients = db.Column(db.String(500), nullable=False)
    category_name = db.Column(db.String(255), nullable = False)

    # Initializing the meals table
    def __init__(self, meal_name:str, recipes:str, ingredients:str, category_name:str):
        self.meal_name = meal_name
        self.recipes = recipes
        self.ingredients = ingredients
        self.category_name = category_name

    # Returning the meals table into json
    def serialize(self):
        return {
            'meal_name':self.meal_name,
            'recipes':self.recipes,
            'ingredients':self.ingredients,
            'category_name':self.category_name
        }
