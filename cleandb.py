import sqlite3

def clean():
    conn = None
    try: 
        conn = sqlite3.connect('iteminfo.db')
        cursor = conn.cursor()

        clean_query = """ DROP TABLE IF EXISTS info;"""

        cursor.execute(clean_query)

        sql_query = """ CREATE TABLE IF NOT EXISTS info (
            id INTEGER PRIMARY KEY,
            itemid text NOT NULL,
            itemname text NOT NULL,
            price text NOT NULL,
            itemimg text NOT NULL
        )"""

        cursor.execute(sql_query)
    except sqlite3.error as e:
            print(e)