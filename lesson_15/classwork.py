from flask import Flask

from sqlalchemy import create_engine

from lesson_14.utils import create_tables
from lesson_14.models import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    users = app.session.query(User).all()
    return [u.as_dict() for u in users]


if __name__ == "__main__":
    engine = create_engine("postgresql://ulitka:ulitka@localhost/ulitka")
    app.session = create_tables(engine)
    app.run()
