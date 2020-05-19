from selenium import webdriver
import unittest


class MockTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_user_start_list(self):
        self.browser.get('http://localhost:8000/')
        self.assertEquals('localhost:8000', self.browser.title)

    def tearDown(self):
        self.browser.quit()


# runs test unit
if __name__ == "__main__":
    unittest.main(warnings='ignore')
