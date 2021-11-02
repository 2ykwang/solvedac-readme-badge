from flask import (
    jsonify
)
from ..solvedac import *
import os


def generate_badge_by_username():
    fetcher = SolvedacFetcher(os.getenv("API_HOST"))
    a = fetcher.get_user_info("csdp000")
    return jsonify(a)


def generate_card_by_username():
    data = jsonify({
        "success": True,
        "result": {
            "username": f""
        }
    })
    return data
