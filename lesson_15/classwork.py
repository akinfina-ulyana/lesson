from flask import Flask, request

from sqlalchemy import create_engine

from lesson_14.utils import create_tables, create_user, find_user
from lesson_14.models import User

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    users = app.session.query(User).all()
    return [u.as_dict() for u in users]


@app.route("/", methods=["POST"])
def post_user():
    user = create_user(app.session, request.form.get("email"), request.form.get("password"))
    return {"user id": user.id}


@app.route("/", methods=["GET"])
def find_some_user():
    user = find_user(app.session, "frog@gmail")
    for data in user:
        return {data}

if __name__ == "__main__":
    engine = create_engine("postgresql://ulitka:ulitka@localhost/ulitka")
    app.session = create_tables(engine)
    app.run()
