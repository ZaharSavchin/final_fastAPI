from fastapi import APIRouter

from app.api.endpoints.note import note_router
from app.api.endpoints.back_call import back_call_router
from app.api.endpoints.pages import pages_router


api_router = APIRouter()

api_router.include_router(note_router)
api_router.include_router(back_call_router)
api_router.include_router(pages_router)
