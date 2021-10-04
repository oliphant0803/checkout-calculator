from os import name
from flask import Flask, render_template, request, jsonify
import sqlite3
import cleandb

app = Flask(__name__)

conn = None
try: 
    conn = sqlite3.connect('iteminfo.db', check_same_thread=False)
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

# def db_connection():
#     conn = None
#     try: 
#         conn = sqlite3.connect('iteminfo.db')
#     except sqlite3.error as e:
#         print(e)
#     return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cart.html/")
def cart():
    return render_template("cart.html")

@app.route("/sum", methods=['POST'])
def sum_num():
    rf=request.form
    data = []
    for key in rf:
        data.append(rf[key])
    print(data)

    sql = """INSERT INTO info (itemid, itemname, price, itemimg)
            VALUES (?, ?, ?, ?)"""
    cursor = conn.execute(sql, (data[0], data[1], data[2], data[3]))
    conn.commit()
    cursor.execute("SELECT * FROM info ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    print(result)
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return 0
    
    return jsonify(len(infos))

@app.route("/addincart", methods=['POST'])
def add():
    rf=request.form
    data = []
    for key in rf:
        data.append(rf[key])
    item_id = data[0]
    cursor = conn.execute("SELECT * FROM info WHERE itemid=?", (item_id,))
    infos =  cursor.fetchone()
    sql = """INSERT INTO info (itemid, itemname, price, itemimg)
            VALUES (?, ?, ?, ?)"""
    cursor = conn.execute(sql, (infos[1], infos[2], infos[3], infos[4]))
    conn.commit()
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return 0
    
    return jsonify(len(infos))

@app.route("/deleteincart", methods=['POST'])
def delete():
    rf=request.form
    data = []
    for key in rf:
        data.append(rf[key])
    item_id = data[0]
    cursor = conn.execute("SELECT * FROM info WHERE itemid=?", (item_id,))
    infos =  cursor.fetchone()
    cursor = conn.execute("DELETE FROM info WHERE id=?", (infos[0],))
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return 0
    return jsonify(len(infos))

@app.route("/removeincart", methods=['POST'])
def remove():
    rf=request.form
    data = []
    for key in rf:
        data.append(rf[key])
    item_id = data[0]
    cursor = conn.execute("DELETE FROM info WHERE itemid=?", (item_id,))
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return 0
    return jsonify(len(infos))
    

@app.route("/cartnum", methods=['POST'])
def cart_num():
    
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return 0
    
    return jsonify(len(infos))

@app.route("/getids", methods=['POST'])
def get_ids():
    
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return []
    counts = {}
    for info in infos:
        if info['itemid'] not in counts:
            counts[info['itemid']] = info['itemid']
    result = list(counts.values())
    print(result)
    return jsonify(result)

@app.route("/getimgs", methods=['POST'])
def get_imgs():
    
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return []
    counts = {}
    for info in infos:
        if info['itemid'] not in counts:
            counts[info['itemid']] = info['itemimg']
    result = list(counts.values())
    print(result)
    return jsonify(result)

@app.route("/getnames", methods=['POST'])
def get_names():
    
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return []
    counts = {}
    for info in infos:
        if info['itemid'] not in counts:
            counts[info['itemid']] = info['name']
    result = list(counts.values())
    print(result)
    return jsonify(result)

@app.route("/getprices", methods=['POST'])
def get_prices():

    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return []
    counts = {}
    for info in infos:
        if info['itemid'] not in counts:
            counts[info['itemid']] = info['price']
    result = list(counts.values())
    print(result)
    return jsonify(result)

@app.route("/getcounts", methods=['POST'])
def get_counts():
    
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return []
    counts = {}
    for info in infos:
        if info['itemid'] not in counts:
            counts[info['itemid']] = 1
        else:
            counts[info['itemid']] += 1
    result = list(counts.values())
    print(result)
    return jsonify(result)

@app.route("/cleandb")
def reset():
    cleandb.clean()
    cursor = conn.execute("SELECT * FROM info")
    infos = [
        dict(id=row[0], itemid=row[1], name=row[2], price=row[3], itemimg=row[4])
        for row in cursor.fetchall()
    ]
    if infos is not None:
        print(infos)
    else:
        return 0
    
    return jsonify(len(infos))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
