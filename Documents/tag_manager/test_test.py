import unittest
from Pages.company_details_page import *
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
        HomePage(self.driver).wait_for_home_page()
        HomePage(self.driver).wait_for_table()
        company_name = HomePage(self.driver).check_table_entry()
        print(company_name)

    def tearDown(self):
            self.driver.close()
