import sqlite3

conn = sqlite3.connect("iteminfo.sqlite")

cursor = conn.cursor()

sql_query = """ DROP TABLE IF EXISTS info;"""

cursor.execute(sql_query)