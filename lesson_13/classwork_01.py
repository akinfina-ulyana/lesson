
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from lesson_12.models import Base, User, Address, Profile

DB_USER = "ulitka"
DB_PASSWORD = "ulitka"
DB_NAME = "ulitka"


def get_user(session, email: str) -> User:
    return session.query(User).filter_by(email=email).first()


if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = get_user(session, "test@test.com")
    if not user:
        user = User(email="test@test.com", password="password")
        session.add(user)

    address = Address(user_id=user.id, city="Minsk", address="Test")
    session.add(address)

    profile = Profile(user_id=user.id, phone="+375292999999", age=20)
    session.add(profile)

    user = session.query(User).filter(User.email == "test@test.com").first()
    user.password = "new_password"
    session.add(user)
    session.commit()

    result = session.query(Profile).filter(Profile.age >= 15)
    for x in result:
        print(x)

    user = User(email="mulika@gmail.com", password="2421555fh")
    session.add(user)
    session.commit()

    user = User(email="shakal@gmail.com", password="gagag3939")
    session.add(user)
    session.commit()

    user = User(email="miha2000@gmail.com", password="1gio23422")
    session.add(user)
    session.commit()

    user = User(email="shagal_13@gmail.com", password="sdfgu6")
    session.add(user)
    session.commit()