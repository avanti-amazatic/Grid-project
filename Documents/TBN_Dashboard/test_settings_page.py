import time

from faker import Faker
from random import randint

import datetime

from re import sub

from decimal import Decimal

from login_code import BaseClass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class LoginTest(BaseClass):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://dev-tbn-dashboard.herokuapp.com/')
        self.login()

    def test_settings(self):
        wait = WebDriverWait(self.driver, 10)

        sidebar_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar-brand')))
        ActionChains(self.driver).move_to_element(sidebar_menu).perform()

        settings_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settings')))

        settings_link.click()

        # Wait until the 'Settings' page is loaded
        search_blog = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-0')))
        search_blog.send_keys('test.com')
        wait.until(EC.visibility_of_element_located((By.ID, 'ul-0')))
        self.driver.find_element_by_css_selector('#ul-0 > li').click()
        bank_name = wait.until(EC.visibility_of_element_located((By.ID, '#input_282')))
        bank_name.clear()
        test_data = Faker()
        bank_name.send_keys(test_data.company())
        accnt_number = self.driver.find_element_by_id('input_283')
        accnt_number.clear()
        accnt_number.send_keys(randint(1000000, 9999999))
        # self.driver.find_element_by_css_selector('')

        routing_number = self.driver.find_element_by_id('input_284')
        routing_number.clear()
        routing_number.send_keys(randint(100, 999))
        # self.driver.find_element_by_css_selector('form.ng-dirty > div:nth-child(5) > button:nth-child(1)')
        toast = self.driver.find_element_by_css_selector('span.ng-binding')
        self.assertTrue(toast.is_displayed())
        self.assertEqual(toast.text, 'SAVED!')

    def test_tax_settings(self):
        test_data = Faker()
        wait = WebDriverWait(self.driver, 10)

        sidebar_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar-brand')))
        ActionChains(self.driver).move_to_element(sidebar_menu).perform()

        settings_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settings')))

        settings_link.click()

        # Wait until the 'Settings' page is loaded
        search_blog = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-0')))
        search_blog.send_keys('test.com')
        wait.until(EC.visibility_of_element_located((By.ID, 'ul-0')))
        self.driver.find_element_by_css_selector('#ul-0 > li').click()
        time.sleep(5)

        # Click on tax information tab
        self.driver.find_element_by_css_selector('md-tab-item.md-tab:nth-child(2) > span:nth-child(1)').click()

        name = wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, 'smart-input[ng-model="bankInfo.bank_name"] > md-input-container > input')))

        # security_number = self.driver.find_element_by_id('input_367')
        # address = self.driver.find_element_by_id('input_368')
        # apartment = self.driver.find_element_by_id('input_369')
        # city = self.driver.find_element_by_id('input_370')
        # state = self.driver.find_element_by_id('input_371')
        # zip = self.driver.find_element_by_id('input_372')

        name.clear()
        name.send_keys(test_data.name())

        # security_number.clear()
        # security_number.send_keys(randint(1000, 9999))
        #
        # address.clear()
        # address.send_keys(test_data.address())
        #
        # apartment.clear()
        # apartment.send_keys(test_data.name())
        #
        # city.clear()
        # city.send_keys(test_data.city())
        #
        # state.clear()
        # state.send_keys(test_data.state())
        #
        # zip.clear()
        # zip.send_keys(randint(1000000, 9999999))

    def tearDown(self):
        self.driver.close()
