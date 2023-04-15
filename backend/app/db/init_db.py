import logging
from sqlalchemy.orm import Session

from app.core.config import Settings
from app.schemas.back_call import BackCallCreateModel
from app.schemas.note import NoteCreateModel

from app.crud.back_call import create_init_back_call
from app.crud.note import create_init_note

settings = Settings()
logger = logging.getLogger('final_fastAPI')


def init_db(db: Session):
    create_back_call(db)
    create_note(db)


def create_back_call(db: Session):

    db_back_call = BackCallCreateModel(
            contacts=settings.INIT_BACK_CALL["contacts"],
            message=settings.INIT_BACK_CALL["message"]
        )
    create_init_back_call(db, db_back_call)


def create_note(db: Session):
    for note in settings.INIT_NOTES:
        db_note = NoteCreateModel(
            title=note['title'],
            text=note['text']
        )
        create_init_note(db, db_note)