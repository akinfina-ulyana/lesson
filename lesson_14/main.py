import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from lesson_14.utils import create_tables

DB_USER = "ulitka"
DB_PASSWORD = "ulitka"
DB_NAME = "ulitka"

if __name__ == "__main__":

    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    session = create_tables(engine)

    logger.info("Hello")