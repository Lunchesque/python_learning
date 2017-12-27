import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
<<<<<<< HEAD
        self.driver.implicitly_wait(1)
=======
>>>>>>> 6fae75bde9c3c33873099cb421214a30612ac5fb

    def test_sech(self):
        driver = self.driver
        driver.get("http://sech.esy.es")

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
