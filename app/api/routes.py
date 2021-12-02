from flask import Blueprint

from . import views

bp = Blueprint("api", __name__)

bp.add_url_rule(
    rule="/badge", view_func=views.generate_badge_by_username, methods=["GET"]
)
# 구버전
bp.add_url_rule(
    rule="/generate/api", view_func=views.generate_badge_by_username, methods=["GET"]
)
