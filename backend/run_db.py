import logging.config

from app.core.config import LOGGING_CONFIG
from app.db.session import SessionLocal
from app.db.init_db import init_db

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('final_fastAPI')


def init():
    db = SessionLocal()
    init_db(db)


def main():
    logger.info('Run initialization')
    init()
    # try:
    #     init()
    # except Exception as error:
    #     logger.error(f"An error during db initialization {error}")
    # else:
    #     logger.info('End initialization')


if __name__ == "__main__":
    main()