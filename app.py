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


# /api/translation?word=adam
@app.route("/api/translation")
def api_get_translation():
    if request.method == 'GET':
        search_word = request.args.get('word')
        cur = get_db().cursor()
        cur.execute("select * from qqen where word = ?", (search_word,))
        result = cur.fetchone()
        return jsonify(id=result["id"], word=result["word"], translation=result["translation"])


# /api/suggestion?begins=a
@app.route("/api/suggestion")
def api_get_suggestion():
    if request.method == 'GET':
        search_word = request.args.get('begins')
        cur = get_db().cursor()
        cur.execute("select word from qqen where word like ? limit 10", (search_word + '%',))
        result = cur.fetchall()
        data = []
        for r in result:
            data.append(r["word"])
        return jsonify(suggestions=data)


# /translate?word=adam
@app.route("/translate")
def get_translate():
    if request.method == 'GET':
        search_word = request.args.get('word')
        cur = get_db().cursor()
        cur.execute("select * from qqen where word = ?", (search_word,))
        result = cur.fetchone()
        return render_template("translate.html", result=result)
