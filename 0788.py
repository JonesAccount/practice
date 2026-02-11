import sqlite3 as sq

with sq.connect("game.db") as con:
    cur = con.cursor()
    tbl = """ CREATE TABLE IF NOT EXISTS users(name TEXT NOT NULL, sex INTEGER NOT NULL) """
    cur.execute(tbl)
    con.commit()

cur.execute("DROP TABLE IF EXISTS sqlite_reguence")
con.commit()

print("Hello")