from flask import Flask, redirect, url_for, render_template, request, jsonify
# from flask_restful import Resource, Api, reqparse
# import pandas as pd
# import ast
import json

app = Flask(__name__)

items = {}

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
    if item_id in items:
        items[item_id] += 1
    else:
        items[item_id] = 1
    number = items.values()
    print(items)
    return str(number)
