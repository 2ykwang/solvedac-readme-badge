import os
import time
from typing import Union

from app import cache
from app.component import make_badge
from app.component.badge import USER_NOT_FOUND
from app.component.options import Options
from app.solvedac import User, get_user_from_dict
from app.solvedac import solvedacfetcher as solved
from flask import Response, current_app, g, make_response, request


# 요청 처리 전
def before_request() -> None:
    g.request_start_time = time.time()


# 렌더링 된 후
def teardown_request(exception) -> None:
    request_time = time.time() - g.request_start_time
    if request_time > 0.4:
        current_app.logger.warning(f"It took `{request_time :.5f}` seconds to respond.")


def generate_badge_by_username():
    username = request.args.get("user")

    options = Options(
        theme=request.args.get("theme", Options.DEFAULT_THEME),
        size=request.args.get("size", Options.DEFAULT_SIZE),
        common_color=request.args.get("common_color", ""),
        sub_color=request.args.get("sub_color", ""),
        back_color=request.args.get("back_color", ""),
        border_color=request.args.get("border_color", ""),
        use_shadow=__bool_parse(request.args.get("use_shadow", "true")),
        is_compact=__bool_parse(request.args.get("compact", "false")),
        use_back_color=__bool_parse(request.args.get("use_back_color", "true")),
        use_border=__bool_parse(request.args.get("use_border", "true")),
    )
    comp = make_badge(None, options)

    if username is None:
        return __make_svg_response(comp.error_render("user 값 확인"), 30)

    cache_max_age = current_app.config["CACHE_CONTROL"]
    timeout = current_app.config["TIMEOUT"]

    # user 생성
    try:

        if cache.get(username) is None:
            cache.set(username, __get_user(username, timeout))
            current_app.logger.info(f"데이터 불러옴: {username}")

        cached_user = cache.get(username)

        comp.user = cached_user

        response = __make_svg_response(comp.render(), cache_max_age)
        return response
    except TimeoutError as e:
        current_app.logger.error(e)
    except Exception as e:
        current_app.logger.warn("generate_badge_by_username -", e)

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


def __bool_parse(text: Union[str, bool]) -> bool:
    return text if type(text) == bool else text.lower() in ["yes", "true", "1", "t"]
