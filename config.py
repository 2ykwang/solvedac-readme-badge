import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    API_HOST = os.getenv("API_HOST") or ""
    TIMEOUT = int(os.getenv("TIMEOUT")) or 30

    # flask cache ( api call )
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = int(os.getenv("CACHE_USER_FETCH")) or 300  # api call cache

    # image cache
    CACHE_CONTROL = int(os.getenv("CACHE_CONTROL")) or 600

    @staticmethod
    def init_app(app):
        pass
