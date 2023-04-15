import os
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = (Path(__file__) / ".." / ".." / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    DB_USER: str
    DB_NAME: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    INIT_NOTES: list = [
        {"title": "моё хобби", "text": "мое любимое занятие - откачивать мед!"},
        {"title": "как я стал пчеловодом", "text": "Меня научил дед. И я читал много книг по пчеловодству"}
    ]

    INIT_BACK_CALL: dict = {"contacts": "+375 29 865 45 62", "message": "Мартин. Хочу купить 2 улья с доставкой в Минск"}
        # {"contacts": "margarin@mail.ru", "message": "стоимость актуальна?"}


    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)-7s %(asctime)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, 'logs', 'api.log'),
            "formatter": "standard",
            "encoding": "UTF-8",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 1000
        }
    },
    "loggers": {
        "final_fastAPI": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        }
    }
}