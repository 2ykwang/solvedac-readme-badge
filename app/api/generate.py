from flask import (
    request,
    make_response,
    Response,
    g
)

from app.component.badge import USER_NOT_FOUND
from ..solvedac import (
    solvedacfetcher as solved,
    get_user_from_dict,
    User,
)

from ..component import (
    make_badge
)
import os
import time


# 요청 처리 전
def before_request() -> None:
    g.request_start_time = time.time()
    g.request_time = time.time() - g.request_start_time


# 렌더링 된 후
def teardown_request(exception) -> None:
    request_time = time.time() - g.request_start_time
    # 렌더링 하는 데 x 초 이상 걸릴 경우
    if request_time > 0.5:
        print(f"It took {request_time :.5f} seconds to respond.")


# def __handle_generate_parameter() ->:
#     username = request.args.get('user')
#
#     if username is None or len(username) < 1:
#
#     # validation


def generate_card_by_username():
    return "test"


def generate_badge_by_username():
    username = request.args.get("user")
    theme = request.args.get("theme", "default")
    component_type = request.args.get("type", "badge")
    is_compact = __bool_parse(request.args.get('compact', 'false'))
    component_size = request.args.get('size', 'small')
    back_color = request.args.get('back_color', '')
    common_color = request.args.get('common_color', "")
    sub_color = request.args.get("sub_color", "")
    border_color = request.args.get("border_color", "")
    use_border = __bool_parse(request.args.get("use_border", "true"))
    use_shadow = __bool_parse(request.args.get("use_shadow", "true"))
    # 뱃지 기본형일 경우 use_back_color 기본값 False
    use_back_color = __bool_parse(
        request.args.get('use_back_color', str(component_type == "card" or (component_type == "badge" and is_compact))))
    # 뱃지 기본형일 경우 use_border 기본값 False
    use_border = __bool_parse(
        request.args.get("use_border", str(component_type == "card" or (component_type == "badge" and is_compact))))

    comp = make_badge(theme, is_compact,
                      user=None,
                      options={'component_size': component_size,
                               'back_color': back_color,
                               'use_back_color': use_back_color,
                               'common_color': common_color,
                               'sub_color': sub_color,
                               'border_color': border_color,
                               'use_border': use_border,
                               'use_shadow': use_shadow,
                               })

    if username is None:
        return __make_svg_response(comp.error_render("user 값 확인"), 30)

    cache_max_age = int(os.getenv("CACHE_CONTROL", 7200))
    timeout = int(os.getenv("TIMEOUT", 15))

    # user 생성
    try:
        comp.user = __get_user(username, timeout)

        response = __make_svg_response(comp.render(), cache_max_age)
        return response
    except TimeoutError as e:
        print(e)
    except Exception as e:
        print("generate_badge_by_username -", e)

    return __make_svg_response(comp.error_render(USER_NOT_FOUND), 30)


def __get_user(username: str, timeout: int = 30) -> User:
    host = os.getenv("API_HOST", "solved.ac")
    fetcher = solved.SolvedacFetcher(host, timeout)
    json_data = fetcher.get_user_info(username)
    user = get_user_from_dict(json_data)
    return user


def __make_svg_response(svg: str, max_age: int = 3600) -> Response:
    response = make_response(svg)
    response.mimetype = "image/svg+xml"
    response.cache_control.public = True
    response.cache_control.max_age = max_age
    return response


def __bool_parse(text: str) -> bool:
    return text.lower() in ["yes", "true", "1", "t"]
