import sqlite3 as sq

with sq.connect("game.db") as con:
    cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
                                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                   name TEXT NOT NULL, sex INTEGER NOT NULL,
                                                   age INTEGER NOT NULL DEFAULT 1,
                                                   old INTEGER DEFAULT 1
               )""")

print("Hello")