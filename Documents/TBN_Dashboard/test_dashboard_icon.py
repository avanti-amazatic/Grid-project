import time

from app_login_code import BaseClass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GeneralPageTests(BaseClass):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://dev-tbn-dashboard.herokuapp.com/')
        self.admin_login()

    def test_zooming_browser(self):
        """
        Zoom in the page to test dashboard icon appearance
        """

        dashboard_icon = self.driver.find_element_by_css_selector('.mdi-navigation-menu')
        sidebar_menu = self.driver.find_element_by_css_selector('.scrollable')

        # Press 'ctrl' and '+' key seven times to attain 200 % zoom
        for zoom_level in range(0, 7):
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, Keys.ADD, Keys.NULL)
            time.sleep(0.5)

        self.assertTrue(dashboard_icon.is_displayed())
        dashboard_icon.click()
        self.assertTrue(sidebar_menu.is_displayed())

    def test_resizing_browser(self):
        """
        Resize browser to test dashboard icon appearance
        """

        # Check that sidebar menu icon as well as the menu is being displayed when window is too small
        self.driver.set_window_size(950, 490)

        dashboard_icon = self.driver.find_element_by_css_selector('.mdi-navigation-menu')
        sidebar_menu = self.driver.find_element_by_css_selector('.scrollable')
        self.assertTrue(dashboard_icon.is_displayed())
        dashboard_icon.click()
        self.assertTrue(sidebar_menu.is_displayed())

    def tearDown(self):
        self.driver.close()