import unittest
import requests

class TestFlask(unittest.TestCase):
    
    def test_web_app_running(self):
        try:
            r = requests.get("http://127.0.0.1:5000/")
        except:
            self.fail("Could not open the web app, testing failed")

    def test_web_title(self):
        r = requests.get("http://127.0.0.1:5000/")
        page_src = r.text
 
        if page_src.find("OLIBAKA") < 0:
            self.fail("Can't find title of web")

    def test_cart_running(self):
        try:
            r = requests.get("http://127.0.0.1:5000/cart.html/")
        except:
            self.fail("Could not open the cart page, testing failed")

    def test_cart_lang(self):
        r = requests.get("http://127.0.0.1:5000/cart.html")
        page_src = r.text
 
        if page_src.find("item") < 0:
            self.fail("Can't find item in web")

        if page_src.find("Cart") < 0:
            self.fail("Can't find cart in web")

        if page_src.find("Summary") < 0:
            self.fail("Can't find summary in web")

        if page_src.find("SHIPPING") < 0:
            self.fail("Can't find shipping in web")

    def test_web_footer(self):
        r = requests.get("http://127.0.0.1:5000/")
        page_src = r.text
        if page_src.find("oliphant0803") < 0:
            self.fail("Can't find oliver in web")

        if page_src.find("kaka0905") < 0:
            self.fail("Can't find katherine in web")

if __name__ == "__main__":
    unittest.main(warnings='ignore', failfast = True)