from flask import Blueprint
from . import (
    generate
)

bp = Blueprint('api', __name__)

bp.add_url_rule(rule='/generate/api', view_func=generate.generate_by_username, methods=["GET"])
bp.before_request(generate.before_request)
bp.teardown_request(generate.teardown_request)
