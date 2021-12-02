import os
import time

from config import Config
from flask import Flask, current_app, g
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

    from .generate import routes as generate

    app.register_blueprint(generate.bp, url_prefix="/")

    app.before_request(before_request)
    app.teardown_request(teardown_request)

    return app


# 요청 처리 전
def before_request() -> None:
    g.request_start_time = time.time()


# 렌더링 된 후
def teardown_request(exception) -> None:
    request_time = time.time() - g.request_start_time
    if request_time > 0.40001:
        current_app.logger.warning(f"It took `{request_time :.5f}` seconds to respond.")
