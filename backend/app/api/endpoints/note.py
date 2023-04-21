import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from app.db.session import get_db
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.schemas.note import NoteModel
from app.models.note import Note, NoteCreate, NoteUpdate
from app.crud.note import get_note_by_id, get_notes_list, create_note, update_note, delete_note


templates = Jinja2Templates(directory="frontend/templates")
note_router = APIRouter()
note_router.mount("/static", StaticFiles(directory="frontend/static"), name="static")
logger = logging.getLogger('final_fastAPI')


@note_router.get("/posts", response_class=HTMLResponse)
async def posts(request: Request, db: Session = Depends(get_db)):
    article = get_notes_list(db)
    return templates.TemplateResponse("posts.html", {"request": request, "article": article})


@note_router.post("/create_new_article", response_class=HTMLResponse)
async def create_note_endpoint(request: Request, title: str = Form(...), text: str = Form(...), db: Session = Depends(get_db)):
    note = NoteCreate(title=title, text=text)
    create_note(db, note)
    return templates.TemplateResponse("post_success.html", {"request": request})


@note_router.get('/create_article', response_class=HTMLResponse)
def create_article_endpoint(request: Request):
    return templates.TemplateResponse("create_article.html", {"request": request})


# @note_router.post('/new_note', response_model=NoteModel)
# def create_note_endpoint(note: NoteCreate, db: Session = Depends(get_db)) -> Note:
#     created_note = create_note(db, note)
#     logger.info(msg=f"Created note {created_note}")
#     return created_note


@note_router.get('/posts/{note_id}', response_class=HTMLResponse)
async def posts(request: Request,note_id: int, db: Session = Depends(get_db)):
    article_detail = get_note_by_id(db, note_id)
    return templates.TemplateResponse("post_detail.html", {"request": request, "article_detail": article_detail})


# @note_router.get('/note/{note_id}', response_model=NoteModel)
# def get_note(note_id: int, db: Session = Depends(get_db)) -> Note:
#     if db_note := get_note_by_id(db, note_id):
#         logger.info(msg=f"Get note {db_note.title}, {db_note.text}")
#         return db_note
#     else:
#         logger.error(f'Note with id={note_id} does\'t exist')
#         raise HTTPException(status_code=404, detail=f'Note with id={note_id} does\'t exist')


@note_router.get('/notes', response_model=List[NoteModel])
async def get_notes(db: Session = Depends(get_db)):
    return get_notes_list(db)





# @note_router.post("/new_back_call", response_class=HTMLResponse)
# async def create_back_call_endpoint(request: Request, contacts: str = Form(...), message: str = Form(...), db: Session = Depends(get_db)):
#     back_call = BackCallCreate(contacts=contacts, message=message)
#     create_back_call(db=db, back_call=back_call)
#     return templates.TemplateResponse("phone_success.html", {"request": request})


@note_router.put('/update_note/{note_id}', response_model=NoteModel)
def update_note_endpoint(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)) -> Note:
    if db_note := get_note_by_id(db, note_id):
        updated_note = update_note(db, db_note, note)
        logger.info(msg=f"Updated note {updated_note}")
        return updated_note
    else:
        logger.error(f"Note does\'t with id={note_id} exist")
        raise HTTPException(status_code=404, detail=f"Note with id={note_id} does\'t  exist")


@note_router.delete('/del_note/{note_id}')
def delete_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    if db_note := get_note_by_id(db, note_id):
        delete_note(db, db_note)
        logger.info(msg=f"Deleted note with id={note_id}")
        return {"detail": f"Note with id={note_id} has been deleted"}
    else:
        logger.error(f"Note does\'t with id={note_id} exist")
        raise HTTPException(status_code=404, detail=f"Note does\'t with id={note_id} exist")