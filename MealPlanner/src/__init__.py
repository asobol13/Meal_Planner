import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = os.environ["SECRET_KEY"],
        SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"],
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        SQLALCHEMY_ECHO = True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent = True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from .models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    # Registering the blueprints
    #from .routes import #accounts, users, meals
    #app.register_blueprint(accounts.bp)
    #app.register_blueprint(users.bp)
    #app.register_blueprint(meals.bp)
    return app