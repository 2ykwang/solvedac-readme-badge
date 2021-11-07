from flask import (
    Flask,
    send_from_directory
)


def create_app():
    app = Flask(__name__)

    from .api import routes as api
    app.register_blueprint(api.bp, url_prefix='/api/v1/')

    @app.route('/<path:path>')
    def route_static_file(path):
        return send_from_directory('static', path)

    return app
