from flask import Flask, redirect, url_for, render_template, request, jsonify
# from flask_restful import Resource, Api, reqparse
# import pandas as pd
# import ast
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

@app.route("/cartnum", methods=['POST'])
def cart_num():
    number = sum(items.values())
    return jsonify(number)

@app.route("/getimgs", methods=['POST'])
def get_imgs():
    pass
@app.route("/getnames", methods=['POST'])
def get_names():
    pass
@app.route("/getprices", methods=['POST'])
def get_prices():
    pass
@app.route("/getcounts", methods=['POST'])
def get_counts():
    pass