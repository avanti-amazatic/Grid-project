import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import *


class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # Page.open('http://dev-tbn-dashboard.herokuapp.com/')
        self.driver.get('http://dev-tbn-dashboard.herokuapp.com/')

    def test_page_load(self):
        LoginPage(self.driver).wait_for_element()
        page = LoginPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_sign_in_button(self):
        MainPage(self.driver).wait_for_button()
        main_page = MainPage(self.driver)
        main_page.click_login_again_button()
        print 'first test case run'

    def test_sign_in_with_valid_user(self):
        page = MainPage(self.driver)
        page.click_login_again_button()
        login_page = LoginPage(self.driver)

        result = login_page.login_with_valid_user("valid_user")
        # self.assertIn("yourstore/home", result.get_url())
        print('second test case run')

    def test_sign_in_with_in_valid_user(self):
        page = MainPage(self.driver)
        page.click_login_again_button()
        login_page = LoginPage(self.driver)
        result = login_page.login_with_in_valid_user("invalid_user")
        # self.assertIn("There was a problem with your request", result)
        print('third test case run')

    def tearDown(self):
        self.driver.close()

# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
#     unittest.TextTestRunner(verbosity=2).run(suite)