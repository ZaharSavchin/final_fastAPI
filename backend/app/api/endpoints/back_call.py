import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.back_call import BackCallModel
from app.models.back_call import BackCall, BackCallCreate
from app.crud.back_call import get_back_call_by_id, get_back_call_list, create_back_call


back_call_router = APIRouter()
logger = logging.getLogger('final_fastAPI')


@back_call_router.get('/back_call/{back_call_id}', response_model=BackCallModel)
def get_note(back_call_id: int, db: Session = Depends(get_db)) -> BackCall:
    if db_back_call := get_back_call_by_id(db, back_call_id):
        logger.info(msg=f"Get back_call {db_back_call.contacts}, {db_back_call.message}")
        return db_back_call
    else:
        logger.error(f'back_call with id={back_call_id} does\'t exist')
        raise HTTPException(status_code=404, detail=f'back_call with id={back_call_id} does\'t exist')


@back_call_router.get('/back_calls', response_model=List[BackCallModel])
async def get_notes(db: Session = Depends(get_db)):
    return get_back_call_list(db)


@back_call_router.post('/new_back_call', response_model=BackCallModel)
def create_back_call_endpoint(note: BackCallCreate, db: Session = Depends(get_db)) -> BackCall:
    back_call = create_back_call(db, note)
    logger.info(msg=f"Created note {back_call}")
    return back_call
