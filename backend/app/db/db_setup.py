from sqlalchemy import create_engine
from app.core.config import Settings
from sqlalchemy.orm import sessionmaker


settings = Settings()

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASS}@' \
                          f'{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)