import multiprocessing
import os

# gunicorn - configuration
wsgi_app = "run:app"
workers = multiprocessing.cpu_count() * 2 + 1
# bind = f'{os.getenv("HOST")}:{os.getenv("PORT")}'

# CMD gunicorn --check--config ./gunicorn.config.py
# CMD gunicorn -c ./gunicorn.config.py
