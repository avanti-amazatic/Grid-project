from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import users
from locators import *


class Page(object):
    """
    This Base class is serving basic attributes for every single page
    inherited from Page class
    """
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://dev-tbn-dashboard.herokuapp.com/'

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_for_element(self, *locator):
        return WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located(*locator))


class MainPage(Page):

    def check_page_loaded(self):
        return True if self.find_element(*MainPageLocators.logo) else False

    def click_login_again_button(self):
        self.driver.find_element(*MainPageLocators.login_again).click()
        return SignUpPage(self.driver)

    def wait_for_button(self):
        return self.wait_for_element(*LoginPageLocators.submit)


class LoginPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*MainPageLocators.logo) else False

    def enter_username(self, user):
        self.driver.find_element(*LoginPageLocators.username).send_keys(
            users.get_user(user)["username"])

    def enter_password(self, user):
        self.driver.find_element(*LoginPageLocators.password).send_keys(
            users.get_user(user)["password"])

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.submit).click()

    def login(self, user):
        self.enter_username(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*LoginPageLocators.error_message).text


class HomePage(Page):
    pass


class SignUpPage(Page):
    pass