import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass(unittest.TestCase):

    def admin_login(self):
        """
        Login Method
        """
        wait = WebDriverWait(self.driver, 10)

        # Wait for page(the one which says 'You are logged out') to load after
        #  entering the URL
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                     '.md-btn')))

        # Click on 'Click here to Login' button and wait for the login page
        # to load
        self.driver.find_element_by_css_selector('.md-btn').click()
        wait.until(EC.visibility_of_element_located((By.ID, 'id_auth-username')))

        self.driver.find_element_by_id('id_auth-username').send_keys(
            'avanti.d@amazatic.com')
        self.driver.find_element_by_id('id_auth-password').send_keys(
            'avanti.d')

        # Click on 'Log in' button and wait for page to load
        self.driver.find_element_by_class_name("btn").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.h4')))