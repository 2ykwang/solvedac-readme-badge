import logging
from typing import Union

from fastapi import Request, Response

from app import cache
from app.component import Options, make_badge
from app.solvedac import SolvedacFetcher, User, get_user_from_dict


def generate_badge_by_username(request: Request) -> Response:
    username = request.query_params.get("user")

    options = Options(
        theme=request.query_params.get("theme", Options.DEFAULT_THEME),
        size=request.query_params.get("size", Options.DEFAULT_SIZE),
        common_color=request.query_params.get("common_color", ""),
        sub_color=request.query_params.get("sub_color", ""),
        back_color=request.query_params.get("back_color", ""),
        border_color=request.query_params.get("border_color", ""),
        use_shadow=_bool_parse(request.query_params.get("use_shadow", "true")),
        is_compact=_bool_parse(request.query_params.get("compact", "true")),
        use_back_color=_bool_parse(request.query_params.get("use_back_color", "true")),
        use_border=_bool_parse(request.query_params.get("use_border", "true")),
    )
    comp = make_badge(None, options)

    config = request.app.state.config
    cache_max_age = config.CACHE_CONTROL
    timeout = config.TIMEOUT

    try:
        if username:
            cached_user = cache.get(username)
            if cached_user is None:
                cached_user = _get_user(username, timeout, config.API_HOST)
                cache[username] = cached_user
                logging.getLogger("uvicorn.error").info(f"데이터 불러옴: {username}")
            comp.user = cached_user
    except Exception as e:
        logging.getLogger("uvicorn.error").error(f"generate_badge_by_username - {e}")

    headers = {"Cache-Control": f"public, max-age={cache_max_age}"}
    return Response(content=comp.render(), media_type="image/svg+xml", headers=headers)


def _get_user(username: str, timeout: int, host: str) -> User:
    fetcher = SolvedacFetcher(host, timeout)
    json_data = fetcher.get_user_info(username)
    return get_user_from_dict(json_data)


def _bool_parse(text: Union[str, bool]) -> bool:
    return text if isinstance(text, bool) else str(text).lower() in ["yes", "true", "1", "t"]
