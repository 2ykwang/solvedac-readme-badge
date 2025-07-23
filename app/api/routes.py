from fastapi import APIRouter
from fastapi.responses import Response

from . import views

router = APIRouter()

router.add_api_route("/badge", views.generate_badge_by_username, methods=["GET"], response_class=Response)
# legacy url
router.add_api_route("/generate/api", views.generate_badge_by_username, methods=["GET"], response_class=Response)
