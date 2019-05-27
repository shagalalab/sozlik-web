#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sqlite3
import sys

con = sqlite3.connect('sozlik.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE dictionary(id INTEGER PRIMARY KEY AUTOINCREMENT, type INTEGER, word TEXT, raw_word TEXT, translation)")

    filename = sys.argv[1]
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO dictionary(word, translation) VALUES(?, ?)", (row['word'].decode('utf8'), row['translation'].decode('utf8')))
