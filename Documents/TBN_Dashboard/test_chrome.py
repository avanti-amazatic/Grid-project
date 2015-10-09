import time

from login_code import BaseClass

from selenium import webdriver


class LoginTest(BaseClass):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get('http://dev-tbn-dashboard.herokuapp.com/')

    def test_login(self):

        self.login_admin()

        self.driver.set_window_size(950, 490)

        time.sleep(1)

        dashboard_icon = self.driver.find_element_by_css_selector('.mdi-navigation-menu')
        sidebar_menu = self.driver.find_element_by_css_selector('.scrollable')
        self.assertTrue(dashboard_icon.is_displayed())
        dashboard_icon.click()
        time.sleep(1)
        self.assertTrue(sidebar_menu.is_displayed())
        self.driver.maximize_window()
        self.driver.find_element_by_id('aside').click()


    def tearDown(self):
        self.driver.close()
