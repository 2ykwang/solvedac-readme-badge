from flask import Blueprint

from . import generate

bp = Blueprint("api", __name__)

# 구버전
bp.add_url_rule(
    rule="/generate/api", view_func=generate.generate_badge_by_username, methods=["GET"]
)
bp.add_url_rule(
    rule="/badge", view_func=generate.generate_badge_by_username, methods=["GET"]
)
bp.add_url_rule(
    rule="/card", view_func=generate.generate_card_by_username, methods=["GET"]
)

bp.before_request(generate.before_request)
bp.teardown_request(generate.teardown_request)
