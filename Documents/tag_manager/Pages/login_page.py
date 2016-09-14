from Pages.Basepage import BasePage
from Pages.Locators import *
from TestData import users


class LoginPage(BasePage):
    """
    This class contains the elements and actions that are present on the login
    page
    """
    def wait_for_login_again_button(self):
        self.wait_for_element(LoginPageLocators.login_again_button)

    def wait_for_login_box(self):
        self.wait_for_element(LoginPageLocators.login_box)

    def enter_username(self):
        self.driver.find_element(*LoginPageLocators.username).send_keys(
            users.username)

    def enter_password(self):
        self.driver.find_element(*LoginPageLocators.password).send_keys(
            users.password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.login_submit).click()

    def click_login_again(self):
        self.driver.find_element(*LoginPageLocators.login_again_button).click()

    def login(self):
        self.wait_for_login_again_button()
        self.click_login_again()
        self.wait_for_login_box()
        self.enter_username()
        self.enter_password()
        self.click_login_button()

    def wait_for_home_page(self):
        self.wait_for_element(HomePageLocators.add_company_button)
