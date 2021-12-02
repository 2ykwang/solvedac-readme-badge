from config import Config
from flask import Flask
from flask_caching import Cache

cache = Cache()


def create_app():
    app = Flask(__name__)

    config = Config()
    app.config.from_object(config)

    config.init_app(app)
    cache.init_app(app)

    from .api import routes as api

    app.register_blueprint(api.bp, url_prefix="/api/v1/")

    return app
