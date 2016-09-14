from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """
    This Base class is serving basic attributes like clicking or typing etc for
     every single page inherited from this BasePage class
    """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://tm3-staging.herokuapp.com/'

    def open(self):
        self.driver.get(self.base_url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def hover_on_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_for_element(self, *locator):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(*locator))

