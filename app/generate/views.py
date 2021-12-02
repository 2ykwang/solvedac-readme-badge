import os
import time

from app.component.options import Options
from app.component.theme import Theme
from flask import current_app, g, render_template, request, url_for


def index():
    theme_list = Theme.get_theme_list()
    size_list = Options.get_size_list()
    return render_template("index.html", themes=theme_list, sizes=size_list)
