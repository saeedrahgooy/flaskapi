from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config
from app.resources.courses import courses_api
from app.resources.reviews import reviews_api

db = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(courses_api)
    app.register_blueprint(reviews_api, url_prefix='/api/v1')
    return app
