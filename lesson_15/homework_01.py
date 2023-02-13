"""
Подключить модели из предыдущего урока, создать для каждой модели
функцию (роут) при помощи flask приложения,
которая принимает POST запрос и создает соответствующий объект и запись в БД.
"""
# дз не сделала

import logging
from flask import Flask, render_template, url_for
import flask_sqlalchemy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/') #обрабатываем главную страницу
@app.route('/home') #дополнительно отслеживаемый URL адресс
def index():
    return render_template("index_1.html")


@app.route('/about')
def about():
    return render_template("about_1.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)




