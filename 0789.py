import sqlite3 as sq

with sq.connect("data0790.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS metrics (
        player TEXT NOT NULL,
        score INTEGER NOT NULL DEFAULT 0
                   )""")

    cur.execute("INSERT INTO metrics (player, score) VALUES ('Julia', 1000)")
    cur.execute("DROP TABLE IF EXISTS metrics")

    cur.execute("""CREATE TABLE IF NOT EXISTS metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player TEXT NOT NULL,
    score INTEGER NOT NULL DEFAULT 5,
    sex INTEGER NOT NULL DEFAULT 2
                )""")
    cur.execute("INSERT INTO metrics (id, player, score, sex) VALUES (1, 'Ellie', 99, 2)")

    con.commit()

    cur.execute("SELECT rowid, * FROM metrics")
    print(cur.fetchall())
    cur.execute("SELECT * FROM metrics")
    print(cur.fetchall())
    cur.execute("SELECT rowid, * FROM metrics")
    #print(cur.fetchmany(1))
    print(cur.fetchone())
    cur.execute("SELECT * FROM metrics")
    print(cur.fetchone()[1])
    cur.execute("SELECT rowid, * FROM metrics")
    els = cur.fetchall()
    els = list(els)
    print("\n" * 4)
    print(els)
    for i in range(len(els)):
        print(els[i])


    els = tuple(els)
    counter = 4
    for el in els:
        print(el[counter])
        counter -= 1