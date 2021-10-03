from copy import deepcopy
import unittest
from flask import jsonify

BASE_URL = 'http://127.0.0.1:5000/'

from os import name
from flask import Flask, render_template, request, jsonify
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

class TestFlaskApi(unittest.TestCase):

    def test_main(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = {'item_id': 1, 'name': "LED bulb 806", 'price': "11.99", "img_src": "/static/assets/1.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "1\n"
            )

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "1\n")

            sent = {'item_id': 1, 'name': "LED bulb 806", 'price': "11.99", "img_src": "/static/assets/1.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "2\n"
            )

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "2\n")

            result = client.post('/getids', data={})
            self.assertEqual(result.data.decode('UTF-8'), '["1"]\n')

            sent = {'item_id': 18, 'name': "Gateway Kit E12", 'price': "99.00", "img_src": "/static/assets/18.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "3\n"
            )

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "3\n")

            result = client.post('/getids', data={})
            self.assertEqual(result.data.decode('UTF-8'), '["1","18"]\n')

            sent = {'item_id': 8, 'name': "Gateway Kit E12", 'price': "25.00", "img_src": "/static/assets/8.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "4\n"
            )

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "4\n")

            result = client.post('/getids', data={})
            self.assertEqual(result.data.decode('UTF-8'), '["1","18","8"]\n')

            result = client.post('/getprices', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[23.98,99.0,25.0]\n')

            sent = {'item_id': 3, 'name': "LED bulb 600", 'price': "14.99", "img_src": "/static/assets/3.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "5\n"
            )

            result = client.post('/getids', data={})
            self.assertEqual(result.data.decode('UTF-8'), '["1","18","8","3"]\n')

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "5\n")

            result = client.post('/getcounts', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[2,1,1,1]\n')

            result = client.post('/getprices', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[23.98,99.0,25.0,14.99]\n')

            sent = {'item_id': 3, 'name': "LED bulb 600", 'price': "14.99", "img_src": "/static/assets/3.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "6\n"
            )

            result = client.post('/getcounts', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[2,1,1,2]\n')

            result = client.post('/getprices', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[23.98,99.0,25.0,29.98]\n')

            result = client.post('/addincart', data={"id": 3})
            self.assertEqual(result.data.decode('UTF-8'), '7\n')

            result = client.post('/getprices', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[23.98,99.0,25.0,44.97]\n')

            result = client.post('/deleteincart', data={"id": 3})
            self.assertEqual(result.data.decode('UTF-8'), '6\n')

            result = client.post('/removeincart', data={"id": 3})
            self.assertEqual(result.data.decode('UTF-8'), '4\n')

    def test_main(self):
        with app.test_client() as client:
            sent = {'item_id': 2, 'name': "LED bulb 800", 'price': "19.99", "img_src": "/static/assets/2.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "1\n"
            )

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "1\n")

            sent = {'item_id': 1, 'name': "LED bulb 806", 'price': "11.99", "img_src": "/static/assets/1.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "2\n"
            )

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "2\n")

            result = client.post('/getids', data={})
            self.assertEqual(result.data.decode('UTF-8'), '["2","1"]\n')

            sent = {'item_id': 13, 'name': "Motion Sensor", 'price': "14.99", "img_src": "/static/assets/13.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "3\n"
            )

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "3\n")

            result = client.post('/getids', data={})
            self.assertEqual(result.data.decode('UTF-8'), '["2","1","13"]\n')

            sent = {'item_id': 1, 'name': "LED bulb 806", 'price': "11.99", "img_src": "/static/assets/1.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "4\n"
            )

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "4\n")

            result = client.post('/getids', data={})
            self.assertEqual(result.data.decode('UTF-8'), '["2","1","13"]\n')

            result = client.post('/getprices', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[19.99,23.98,14.99]\n')

            sent = {'item_id': 3, 'name': "LED bulb 600", 'price': "14.99", "img_src": "/static/assets/3.png"}
            result = client.post(
                '/sum',
                data=sent
            )
            self.assertEqual(
                result.data.decode('UTF-8'),
                "5\n"
            )

            result = client.post('/getids', data={})
            self.assertEqual(result.data.decode('UTF-8'), '["2","1","13","3"]\n')

            result = client.post('/cartnum', data={})
            self.assertEqual(result.data.decode('UTF-8'), "5\n")

            result = client.post('/getcounts', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[1,2,1,1]\n')

            result = client.post('/getprices', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[19.99,23.98,14.99,14.99]\n')

            result = client.post('/addincart', data={"id": 1})
            self.assertEqual(result.data.decode('UTF-8'), '6\n')

            result = client.post('/deleteincart', data={"id": 1})
            self.assertEqual(result.data.decode('UTF-8'), '5\n')

            result = client.post('/removeincart', data={"id": 1})
            self.assertEqual(result.data.decode('UTF-8'), '3\n')

            result = client.post('/removeincart', data={"id": 2})
            self.assertEqual(result.data.decode('UTF-8'), '2\n')

            result = client.post('/getcounts', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[1,1]\n')

            result = client.post('/getprices', data={})
            self.assertEqual(result.data.decode('UTF-8'), '[14.99,14.99]\n')

if __name__ == "__main__":
    unittest.main()