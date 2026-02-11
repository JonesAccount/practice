import sqlite3 as sq

import sqlite3 as sq

with sq.connect("data.db") as con:
    cur = con.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS users
                (
                    id
                    INTEGER
                    PRIMARY
                    KEY
                    AUTOINCREMENT,
                    name
                    TEXT
                    NOT
                    NULL,
                    sex
                    INTEGER
                    NOT
                    NULL
                    DEFAULT
                    1,
                    old
                    INTEGER
                    NOT
                    NULL
                    DEFAULT
                    1,
                    score
                    INTEGER
                    NOT
                    NULL
                    DEFAULT
                    0
                )
                """)

    con.commit()