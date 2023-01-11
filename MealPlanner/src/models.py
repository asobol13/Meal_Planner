from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Setting up the class for accounts table
class Account(db.Model):
    __tablename__='accounts'
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    user_key = db.Column(db.String(255), nullable=False)

# Setting up the class for users table
class User(db.Model):
    __tablename__='users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    dietary_restrictions = db.Column(db.Boolean, nullable=True, default=False)

#Setting up the class for meals table
class Meal(db.Model):
    __tablename__='meals'
    meal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meal_name = db.Column(db.String(255), nullable=False)
    recipes = db.Column(db.String(255), nullable = False)
    ingredients = db.Column(db.String(500), nullable=False)