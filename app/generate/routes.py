from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from . import views

router = APIRouter()

router.add_api_route("/", views.index, methods=["GET"], response_class=HTMLResponse)
