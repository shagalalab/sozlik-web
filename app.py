import sqlite3
from flask import Flask, render_template, g, request, jsonify

app = Flask(__name__)

DATABASE = '/Users/atabek/Projects/Flask/sozlik.com/sozlik/sozlik.db'


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


# /api/translation/<word>
@app.route("/api/translation/<search_word>")
def api_get_translation(search_word):
    cur = get_db().cursor()
    cur.execute("select * from qqen where word = ?", (search_word,))
    result = cur.fetchone()
    return jsonify(id=result["id"], word=result["word"], translation=result["translation"])


# /api/suggestion/<beginswith>
@app.route("/api/suggestion/<beginswith>")
def api_get_suggestion(beginswith):
    cur = get_db().cursor()
    cur.execute("select word from qqen where word like ? limit 10", (beginswith + '%',))
    result = cur.fetchall()
    data = []
    for r in result:
        data.append(r["word"])
    return jsonify(suggestions=data)


# /translate/<search_word>
@app.route("/translate/<search_word>")
def get_translate(search_word):
    cur = get_db().cursor()
    cur.execute("select * from qqen where word = ?", (search_word,))
    result = cur.fetchone()
    return render_template("translate.html", word=result["word"], translation=result["translation"])
