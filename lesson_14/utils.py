from sqlalchemy.orm import sessionmaker
from lesson_13.models import Base
from lesson_13.models import User, Address, Profile


def create_tables(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def create_user(session, email, password):
    user = User(email=email, password=password)

    session.add(user)
    session.commit()

    return user


def find_user(session, email):
    return session.query(User).filter(User.email == email).first()


def user_check(session, email: str) -> User:
    return session.query(User).filter(email=email).first()


def user_address(session, user, city, address):
    address = Address(user=user.id, city=city, address=address)

    session.add(address)
    session.commit()


def user_profile(session, user_id, phone, age):
    profile = Profile(user_id=user.id, phone=phone, age=age)

    session.add(profile)
    session.commit()
