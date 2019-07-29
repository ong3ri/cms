import os

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import configuration
from manage import init_commands


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.static_folder = os.getenv('STATIC_FOLDER')
    app.debug = True
    app.config.from_object(configuration[config_name])

    db.init_app(app)
    migrate.init_app(app, db=db)

    from app.api import cms
    app.register_blueprint(cms, url_prefix='/api/')

    init_commands(app)

    return app
