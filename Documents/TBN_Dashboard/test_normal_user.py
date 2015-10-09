import time

import datetime

from re import sub

from decimal import Decimal

from login_code import BaseClass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class LoginTest(BaseClass):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://dev-tbn-dashboard.herokuapp.com/')
        self.login_normal_user()

    def test_calc(self):
        wait = WebDriverWait(self.driver, 10)

        # Wait for 'Key performance index' card to load
        wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, 'md-grid-tile.kpi:nth-child(1) > figure:nth-child(1) > div:nth-child(1)')))