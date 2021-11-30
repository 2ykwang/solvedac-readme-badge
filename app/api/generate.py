import os
import time

from app import cache
from app.component import make_badge
from app.component.badge import USER_NOT_FOUND
from app.solvedac import User, get_user_from_dict
from app.solvedac import solvedacfetcher as solved
from flask import Response, current_app, g, make_response, request


# 요청 처리 전
def before_request() -> None:
    g.request_start_time = time.time()


# 렌더링 된 후
def teardown_request(exception) -> None:
    request_time = time.time() - g.request_start_time
    if request_time > 0.05:
        print(f"It took `{request_time :.5f}` seconds to respond.")


def generate_badge_by_username():
    username = request.args.get("user")
    theme = request.args.get("theme", "default")
    component_type = request.args.get("type", "badge")
    is_compact = __bool_parse(request.args.get("compact", "false"))
    component_size = request.args.get("size", "small")
    back_color = request.args.get("back_color", "")
    common_color = request.args.get("common_color", "")
    sub_color = request.args.get("sub_color", "")
    border_color = request.args.get("border_color", "")
    use_border = __bool_parse(request.args.get("use_border", "true"))
    use_shadow = __bool_parse(request.args.get("use_shadow", "true"))
    # 뱃지 기본형일 경우 use_back_color 기본값 False
    use_back_color = __bool_parse(
        request.args.get(
            "use_back_color",
            str(component_type == "card" or (component_type == "badge" and is_compact)),
        )
    )
    # 뱃지 기본형일 경우 use_border 기본값 False
    use_border = __bool_parse(
        request.args.get(
            "use_border",
            str(component_type == "card" or (component_type == "badge" and is_compact)),
        )
    )

    comp = make_badge(
        theme,
        is_compact,
        user=None,
        options={
            "component_size": component_size,
            "back_color": back_color,
            "use_back_color": use_back_color,
            "common_color": common_color,
            "sub_color": sub_color,
            "border_color": border_color,
            "use_border": use_border,
            "use_shadow": use_shadow,
        },
    )

    if username is None:
        return __make_svg_response(comp.error_render("user 값 확인"), 30)

    cache_max_age = current_app.config["CACHE_CONTROL"]
    timeout = current_app.config["TIMEOUT"]

    # user 생성
    try:

        cached_user = cache.get(username)
        if cached_user is None:
            cache.set(
                username,
                __get_user(username, timeout),
                timeout=current_app.config["CACHE_DEFAULT_TIMEOUT"],
            )
            print(f"데이터 불러옴: {username}")

        comp.user = cached_user

        response = __make_svg_response(comp.render(), cache_max_age)
        return response
    except TimeoutError as e:
        print(e)
    except Exception as e:
        print("generate_badge_by_username -", e)

    return __make_svg_response(comp.error_render(USER_NOT_FOUND), 30)


def __get_user(username: str, timeout: int = 30) -> User:
    host = current_app.config["API_HOST"]
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
