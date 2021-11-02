from flask import (
    jsonify
)


def generate_badge_by_username():
    data = jsonify({
        "success": True,
        "result": {
            "username": f""
        }
    })
    return data


def generate_card_by_username():
    data = jsonify({
        "success": True,
        "result": {
            "username": f""
        }
    })
    return data
