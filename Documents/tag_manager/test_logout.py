import unittest
from selenium import webdriver
from Pages.Basepage import *
from Pages.login_page import *
from selenium.webdriver.chrome.options import Options
from Pages.home_page import *

class TestPages(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        BasePage(self.driver).open()

    def test_login_with_valid_user(self):
        LoginPage(self.driver).login()
        HomePage(self.driver).wait_for_home_page()
        HomePage(self.driver).click_on_logout()
        LoginPage(self.driver).wait_for_login_box()

    def tearDown(self):
            self.driver.close()
