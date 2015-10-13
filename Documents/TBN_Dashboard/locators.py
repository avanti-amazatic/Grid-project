from selenium.webdriver.common.by import By


class MainPageLocators(object):
    logo = (By.CSS_SELECTOR, '.form-signin-heading > a > img')
    login_again = (By.CSS_SELECTOR, '.md-btn')


class LoginPageLocators(object):
    username = (By.ID, 'id_auth-username')
    password = (By.ID, 'id_auth-password')
    submit = (By.CLASS_NAME, 'btn')
    error_message = (By.CSS_SELECTOR, '.errorlist > li')

