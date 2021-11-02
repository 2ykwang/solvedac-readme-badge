from flask import (
    jsonify,
    request,
    render_template,
    g
)
from ..solvedac import (
    SolvedacFetcher as solved,
    tier,
    Badge,
    User,
)
import os
import time


# 요청 처리 전
def before_request():
    g.request_start_time = time.time()
    g.request_time = time.time() - g.request_start_time


# 렌더링 된 후
def teardown_request(exception):
    request_time = time.time() - g.request_start_time
    # 렌더링 하는 데 x 초 이상 걸릴 경우
    if request_time > 1.0:
        print(f"It took {request_time :.5f} seconds to respond.")


def generate_badge_by_username():
    username = request.args.get('user')

    if username is None:
        return "error"

    # api 호출
    fetcher = solved.SolvedacFetcher(os.getenv("API_HOST"))
    json_data = fetcher.get_user_info(username)

    # user 생성
    user = User.get_user_from_dict(json_data)

    # badge 생성
    card = make_badge(user)

    return card


def make_badge(user: User) -> str:
    ee = render_template("badge_small.svg",
                         tier_icon=tier.tier_icon[ user.tier],
                         username=user.username
                         )
    print(user.username)
    return ee


def generate_card_by_username():
    data = jsonify({
        "success": True,
        "result": {
            "username": f""
        }
    })
    return data
