from flask import Flask


def create_app():
    app = Flask(__name__)

    from .api import routes as api

    app.register_blueprint(api.bp, url_prefix="/api/v1/")

    return app
