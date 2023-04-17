# templates.TemplateResponse
from fastapi import APIRouter

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="PycharmProjects/final_fastAPI/frontend/templates")
pages_router = APIRouter()


@pages_router.get("/", response_class=HTMLResponse)
async def index():
    context = {"request": 'main'}
    return templates.TemplateResponse("index.html", context=context)