import logging
from typing import List

from sqlalchemy.orm import Session
from app.models.back_call import BackCall, BackCallCreate


logger = logging.getLogger('final_fastAPI')


def create_init_back_call(db: Session, back_call: BackCall) -> BackCall:
    db_back_call = BackCall(
        contacts=back_call.contacts,
        message=back_call.message
    )
    db.add(db_back_call)
    db.commit()
    db.refresh(db_back_call)
    logger.info(f'Created author {db_back_call}')
    return db_back_call


def get_back_call_by_id(db: Session, id_: int) -> BackCall:
    return db.query(BackCall).filter(BackCall.id == id_).first()


def get_back_call_list(db: Session) -> List[BackCall]:
    return db.query(BackCall).all()


def create_back_call(db: Session, back_call: BackCallCreate) -> BackCall:
    db_back_call = BackCall(**back_call.dict())
    db.add(db_back_call)
    db.commit()
    db.refresh(db_back_call)
    return db_back_call
