from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.support import expected_conditions as EC


class OnFirefox (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)

    def test_Google_Search_FF(self):
        driver = self.driver
        driver.get("http://www.google.com")
        input_element = driver.find_element_by_name("q")
        input_element.send_keys("Cheese!")
        input_element.submit()
        WebDriverWait(driver, 20).until(EC.title_contains("Cheese! - Google Search"))
        self.assertEqual("Cheese! - Google Search", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
