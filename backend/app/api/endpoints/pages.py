# templates.TemplateResponse
from fastapi import APIRouter
from fastapi import Request
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="frontend/templates")
pages_router = APIRouter()
pages_router.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@pages_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@pages_router.get("/contacts", response_class=HTMLResponse)
async def contacts(request: Request):
    return templates.TemplateResponse("contacts.html", {"request": request})


@pages_router.get("/delivery", response_class=HTMLResponse)
async def delivery(request: Request):
    return templates.TemplateResponse("delivery.html", {"request": request})


@pages_router.get("/articles", response_class=HTMLResponse)
async def articles(request: Request):
    return templates.TemplateResponse("articles.html", {"request": request})


@pages_router.get("/images_bee_trap", response_class=HTMLResponse)
async def images_bee_trap(request: Request):
    return templates.TemplateResponse("images_bee_trap.html", {"request": request})


@pages_router.get("/images_bee_hive", response_class=HTMLResponse)
async def images_bee_hive(request: Request):
    return templates.TemplateResponse("images_bee_hive.html", {"request": request})


@pages_router.get("/beehaves", response_class=HTMLResponse)
async def beehaves(request: Request):
    return templates.TemplateResponse("beehaves.html", {"request": request})


@pages_router.get("/catch_bees", response_class=HTMLResponse)
async def catch_bees(request: Request):
    return templates.TemplateResponse("catch_bees.html", {"request": request})


@pages_router.get("/description_bee_hive", response_class=HTMLResponse)
async def description_bee_hive(request: Request):
    return templates.TemplateResponse("description_bee_hive.html", {"request": request})


@pages_router.get("/price_bee_hive", response_class=HTMLResponse)
async def price_bee_hive(request: Request):
    return templates.TemplateResponse("price_bee_hive.html", {"request": request})


@pages_router.get("/description_bee_trap", response_class=HTMLResponse)
async def description_bee_trap(request: Request):
    return templates.TemplateResponse("description_bee_trap.html", {"request": request})


@pages_router.get("/price_bee_trap", response_class=HTMLResponse)
async def price_bee_trap(request: Request):
    return templates.TemplateResponse("price_bee_trap.html", {"request": request})


@pages_router.get("/price_bee_trap", response_class=HTMLResponse)
async def price_bee_trap(request: Request):
    return templates.TemplateResponse("price_bee_trap.html", {"request": request})
