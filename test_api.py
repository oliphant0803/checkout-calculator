from copy import deepcopy
import unittest
from flask import jsonify
from app import app

BASE_URL = 'http://127.0.0.1:5000/'


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