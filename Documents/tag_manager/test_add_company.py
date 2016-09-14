import unittest
from selenium import webdriver
from Pages.Basepage import *
from Pages.login_page import *
from selenium.webdriver.chrome.options import Options
from Pages.home_page import *
import faker
f = faker.Faker()
import time


class TestPages(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        BasePage(self.driver).open()

    def test_create_company(self):
        LoginPage(self.driver).login()
        LoginPage(self.driver).wait_for_home_page()
        HomePage(self.driver).click_on_add_company()
        HomePage(self.driver).wait_for_create_company_page()
        HomePage(self.driver).enter_company_name()
        HomePage(self.driver).click_on_create_button()


    # def tearDown(self):
    #         self.driver.close()

