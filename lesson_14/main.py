import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from lesson_14.utils import create_tables, create_user, find_user, user_check, user_address, user_profile

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


    menu = """
        1. создать пользователя
        2. Найти пользователя
        3. exit
        """
    while True:
        logger.info(menu)
        choice = input("Введите функцию: 1- создание пользователя")
        if choice == "1":
            email = input("Введите email")
            password = input("Введите password")
            if email == user_check(session, email):
                logger.info("Пользователь существует, введите другой email")
                continue
            #password = input("Введите password")

            elif user == create_user(session, email, password):
                logger.info(f"User #{user.id} is created")



        elif choice == "2":
            email = input("Введите email")
            user = find_user(session, email)
            logger.info(f"User #{user.id}")

        elif choice == "4":
            user = input("Введите user.id")
            city = input("Введите ваш город")
            address = input("Введите ваш адрес")
            user = user_address(session, user, city, address)
            logger.info(f"User #{user.id} is created")

        elif choice == "5":
            user_id = input("Введите user.id")
            phone = input("Введите номер телефона")
            age = input("Введите ваш возраст")

        elif choice == "3":
            exit()

