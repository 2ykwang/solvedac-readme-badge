from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.component.options import Options
from app.component.theme import Theme
from app import templates


def index(request: Request) -> HTMLResponse:
    theme_list = list(Theme.get_theme_list())
    size_list = Options.get_size_list()
    return templates.TemplateResponse(
        "index.html", {"request": request, "themes": theme_list, "sizes": size_list}
    )
