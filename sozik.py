#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sqlite3

from flask import Flask, render_template, g, jsonify

from util.spell import candidates

app = Flask(__name__)

DATABASE = app.root_path + '/db/sozlik.db'


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


# /api/suggestion/<beginswith>
@app.route("/api/suggestion/<beginswith>")
def api_get_suggestion(beginswith):
    beginswith = normalize_query(beginswith)
    cur = get_db().cursor()
    cur.execute("select * from dictionary where word like ? limit 10", (beginswith + '%',))
    result = cur.fetchall()
    data = []
    if result:
        for r in result:
            data.append({
                'word': r['word'],
                'type': r['type'],
                'raw_word': r['raw_word'],
                'id': r['id']
            })
    return jsonify(suggestions=data)


# /translate/<dictionary_type>/<search_word>
@app.route("/translate/<dictionary_type>/<search_word>")
def get_translate(dictionary_type, search_word):
    search_word = normalize_query(search_word)
    dictionary_id = None
    if dictionary_type == 'qqen':
        dictionary_id = 1
    elif dictionary_type == 'ruqq':
        dictionary_id = 2
    cur = get_db().cursor()
    if dictionary_id:
        cur.execute("select * from dictionary where word = ? AND type = ?", (search_word, dictionary_id))
    else:
        cur.execute("select * from dictionary where word = ?", (search_word,))
    result = cur.fetchone()
    if result and result["type"] == 1:
        return render_template("translate.html", img_src="/static/images/qqen.png", word=result["raw_word"], translation=result["translation"])
    elif result and result["type"] == 2:
        return render_template("translate.html", img_src="/static/images/ruqq.png", word=result["raw_word"], translation=result["translation"])
    else:
        did_you_mean = candidates(search_word, get_all_words())
        return render_template("notfound.html", word=search_word, did_you_mean=did_you_mean)


def normalize_query(search_word):
    return re.sub(u'[^a-záúıóǵńA-ZÁÚÍÓǴŃа-яёәүқөғңА-ЯЁӘҮҚӨҒҢ\-]', '', search_word.lower())


def get_all_words():
    data = []
    cur = get_db().cursor()
    cur.execute("select word from dictionary")
    result = cur.fetchall()
    if result:
        for r in result:
            data.append(r["word"])
    return data
