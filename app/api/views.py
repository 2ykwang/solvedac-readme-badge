import os

from typing import Union

from app import cache
from app.component import Options, make_badge
from app.solvedac import SolvedacFetcher, User, get_user_from_dict
from flask import Response, current_app, g, make_response, request


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
        is_compact=__bool_parse(request.args.get("compact", "true")),
        use_back_color=__bool_parse(request.args.get("use_back_color", "true")),
        use_border=__bool_parse(request.args.get("use_border", "true")),
    )
    comp = make_badge(None, options)

    cache_max_age = current_app.config["CACHE_CONTROL"]
    timeout = current_app.config["TIMEOUT"]

    # user 생성
    try:
        if cache.get(username) is None:
            cache.set(username, __get_user(username, timeout))
            current_app.logger.info(f"데이터 불러옴: {username}")

        cached_user = cache.get(username)
        comp.user = cached_user
    except Exception as e:
        current_app.logger.error(f"generate_badge_by_username - {e}")

    return __make_svg_response(comp.render(), cache_max_age)


def __get_user(username: str, timeout: int = 30) -> User:
    host = current_app.config["API_HOST"]
    fetcher = SolvedacFetcher(host, timeout)
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
