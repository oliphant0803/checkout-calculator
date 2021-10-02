from os import name
from flask import Flask, redirect, url_for, render_template, request, jsonify
import json

app = Flask(__name__)

items = {}
info = {}

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
    item_id = data[0]
    if item_id not in info:
        info[item_id] = (data[1], data[2], data[3])
    if item_id in items:
        items[item_id] += 1
    else:
        items[item_id] = 1
    number = sum(items.values())
    print(items)
    print(info)
    return jsonify(number)

@app.route("/addincart", methods=['POST'])
def add():
    rf=request.form
    data = []
    for key in rf:
        data.append(rf[key])
    item_id = data[0]
    items[item_id] += 1
    number = sum(items.values())
    return jsonify(number)

@app.route("/deleteincart", methods=['POST'])
def delete():
    rf=request.form
    data = []
    for key in rf:
        data.append(rf[key])
    item_id = data[0]
    if items[item_id] == 1:
        del items[item_id]
        del info[item_id]
    else:
        items[item_id] -= 1
    number = sum(items.values())
    return jsonify(number)

@app.route("/removeincart", methods=['POST'])
def remove():
    rf=request.form
    data = []
    for key in rf:
        data.append(rf[key])
    item_id = data[0]
    del items[item_id]
    del info[item_id]
    number = sum(items.values())
    return jsonify(number)

@app.route("/cartnum", methods=['POST'])
def cart_num():
    number = sum(items.values())
    return jsonify(number)

@app.route("/getids", methods=['POST'])
def get_ids():
    ids = []
    for item_id in items:
        ids.append(item_id)
    return jsonify(ids)

@app.route("/getimgs", methods=['POST'])
def get_imgs():
    imgs = []
    for item_id in info:
        imgs.append(info[item_id][2])
    return jsonify(imgs)

@app.route("/getnames", methods=['POST'])
def get_names():
    names = []
    for item_id in info:
        names.append(info[item_id][0])
    return jsonify(names)

@app.route("/getprices", methods=['POST'])
def get_prices():
    prices = []
    for item_id in info:
        prices.append(float(info[item_id][1]) * float(items[item_id]))
    return jsonify(prices)

@app.route("/getcounts", methods=['POST'])
def get_counts():
    counts = []
    for item_id in items:
        counts.append(items[item_id])
    return jsonify(counts)