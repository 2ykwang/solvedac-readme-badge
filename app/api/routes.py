from flask import Blueprint
from . import (
    generate
)

bp = Blueprint('api', __name__)

bp.add_url_rule(rule='/generate/badge', view_func=generate.generate_badge_by_username, methods=["GET"])
bp.add_url_rule(rule='/generate/card', view_func=generate.generate_card_by_username, methods=["GET"])