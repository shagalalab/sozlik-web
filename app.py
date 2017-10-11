import os
import sqlite3
from flask import Flask, render_template, g

app = Flask(__name__)
app.debug = True

DATABASE = os.getcwd() + '/sozlik.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/translation")
def api_get_translation():
    cur = get_db().cursor()
    cur.execute("select * from qqen")
    result = cur.fetchone()
    return render_template("word.html", result=result)


# /api/translation?word=adam
# /api/suggestion?begins=a
# /translate?word=adam
