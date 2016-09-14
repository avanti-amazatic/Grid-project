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
        HomePage(self.driver).click_on_add_company()
        HomePage(self.driver).wait_for_create_company_page()
        company_test_data = HomePage(self.driver).enter_company_name()
        HomePage(self.driver).click_on_create_button()
        CompanyDetailsPage(self.driver).wait_for_company_detail_page()
        CompanyDetailsPage(self.driver).enter_url()
        CompanyDetailsPage(self.driver).enter_inventory()
        CompanyDetailsPage(self.driver).click_on_save()
        time.sleep(3)
        CompanyDetailsPage(self.driver).go_back_on_accounts()
        HomePage(self.driver).wait_for_table()
        company_name = HomePage(self.driver).check_table_entry()
        self.assertEqual(company_name, company_test_data)

    def tearDown(self):
            self.driver.close()
