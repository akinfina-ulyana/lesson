import sqlite3

def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO user (firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
           (firstname, lastname, email, password, age),
       )
       session.commit()



if __name__ == "__main__":

    create_user("Uly", "Ulitka", "uly.ulitka@gmail.com", "TestPass", 20)
    create_user("Fly", "Flitka", "fly.flitka@gmail.com", "TestPass", 17)
    create_user("Di", "Dina", "di.dina@gmail.com", "TestPass", 30)
    create_user("Abra", "Abel", "abra.abel@gmail.com", "TestPass", 18)


def select_user(email: str):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user
           WHERE email = ?;
           """,
           (email,)
       )
       session.commit()
       return cursor.fetchone()


select_user("manti.by@gmail.com")











