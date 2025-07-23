import logging
import time

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from cachetools import TTLCache

from config import Config

cache = TTLCache(maxsize=1024, ttl=Config.CACHE_DEFAULT_TIMEOUT)
templates = Jinja2Templates(directory="app/templates")


def create_app() -> FastAPI:
    config = Config()
    app = FastAPI()

    app.state.config = config
    app.state.cache = cache
    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    from .api import routes as api
    from .generate import routes as generate

    app.include_router(api.router, prefix="/api/v1")
    app.include_router(generate.router)

    Config.init_app(logging.getLogger("uvicorn.error"))

    @app.middleware("http")
    async def log_slow_requests(request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        if duration > 0.40001:
            logging.getLogger("uvicorn.error").warning(
                f"It took `{duration :.5f}` seconds to respond."
            )
        return response

    return app
