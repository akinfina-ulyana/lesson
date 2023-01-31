from pathlib import Path
from sqlalchemy import create_engine  # для конекта к бд
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from lesson_12.models import Base, User

DB_PATH = Path(__file__).resolve().parent / "my_database.sqlite3" # имя базы ???
DB_ECHO = True


if __name__ == "__main__":
    engine = create_engine(f"sqlite:////{DB_PATH}", echo=DB_ECHO) # для конекта к бд
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)     # отвечает за создание таблиц в бд
    Session = sessionmaker(bind=engine)  # отвечает за создание сессии по средствам которой можем записывать данные в бд
    session = Session()                  # короче для совершения действий с бд

    user = User(email="test@test.com", password="password")
    session.add(user)
    session.commit()