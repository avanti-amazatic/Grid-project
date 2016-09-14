from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    login_box = (By.CSS_SELECTOR, '.login-box')
    login_again_button = (By.CSS_SELECTOR, 'button.btn.btn-primary')
    username = (By.ID, 'id_auth-username')
    password = (By.ID, 'id_auth-password')
    login_submit = (By.CSS_SELECTOR, 'button.btn-primary')


class HomePageLocators():
    add_company_button = (By.CSS_SELECTOR, 'a.btn.btn-info')
    logout_button = (By.CSS_SELECTOR, 'div.header-link:nth-child(2)')
    table = (By.CSS_SELECTOR, '#wrapper > div > div > div.hpanel > div > div > div:nth-child(2) > div > table > tbody')
    table_row_load = (By.CSS_SELECTOR, '#wrapper > div > div > div.hpanel > div > div > div:nth-child(2) > div > table > tbody > tr:nth-child(1)')
    table_rows = (By.TAG_NAME, 'tr')
    table_content = (By.TAG_NAME, 'td')


class CreateCompanyLocators():
    create_button = (By.CSS_SELECTOR, 'button.btn.btn-sm')
    company_name = (By.ID, 'name')


class CreateCompanyDetails():
    url = (By.NAME, 'url')
    inventory = (By.NAME, 'inventory_name')
    save_button = (By.CSS_SELECTOR, 'button.btn.pull-right')
    toast = (By.CSS_SELECTOR, '#toast-container')
    back_on_accounts = (By.CSS_SELECTOR, '#hbreadcrumb > ol > li:nth-child(1) > span > a')
