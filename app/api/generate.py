from flask import (
    request,
    make_response,
    Response,
    g
)
from ..solvedac import (
    SolvedacFetcher as solved,
    solvedac_badge,
    User,
)
from ..component import (
    Badge
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
    if request_time > 0.5:
        print(f"It took {request_time :.5f} seconds to respond.")


def generate_by_username():
    username = request.args.get('user')
    component_type = request.args.get('type')
    is_compact = request.args.get('compact')

    error_comp = Badge
    if component_type is not None:
        if component_type == "card":
            error_comp = Badge
        elif component_type == "badge":
            error_comp = Badge

    if is_compact is None:
        is_compact = False
    else:
        is_compact = bool(is_compact)

    if username is None:
        return __make_svg_response(error_comp.error_render("can't find user"), 30)

    cache_max_age = int(os.getenv("CACHE_CONTROL"))

    # user 생성
    try:
        user = __get_user(username)
        # badge 생성
        comp = solvedac_badge.make_badge(user, is_compact)
        if component_type == "badge":
            comp = solvedac_badge.make_badge(user, is_compact)
        elif component_type == "card":
            comp = solvedac_badge.make_badge(user, is_compact)

        response = __make_svg_response(comp, cache_max_age)

        return response

    except Exception as e:
        print("generate_badge_by_username -", e)

    return __make_svg_response(error_comp.error_render("unknown users"), 30)


def __get_user(username: str) -> User:
    host = os.getenv("API_HOST")
    fetcher = solved.SolvedacFetcher(host)
    json_data = fetcher.get_user_info(username)
    user = User.get_user_from_dict(json_data)
    return user


def __make_svg_response(svg, max_age: int = 3600) -> Response:
    response = make_response(svg)
    response.mimetype = "image/svg+xml"
    response.cache_control.public = True
    response.cache_control.max_age = max_age
    return response
