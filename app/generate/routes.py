from flask import Blueprint

from . import views

bp = Blueprint("generate", __name__)

bp.add_url_rule(rule="/", view_func=views.index, methods=["GET"])
