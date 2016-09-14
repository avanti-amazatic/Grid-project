import unittest
from selenium import webdriver
from Pages.login_page import *
from selenium.webdriver.chrome.options import Options
from Pages.home_page import *
import time
from Pages.company_details_page import *


class TestPages(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        BasePage(self.driver).open()

    def test_add_company(self):
        LoginPage(self.driver).login()
        HomePage(self.driver).wait_for_home_page()
        HomePage(self.driver).pick_up_first_entry()
        CompanyDetailsPage(self.driver).wait_for_company_detail_page()

    def tearDown(self):
            self.driver.close()
