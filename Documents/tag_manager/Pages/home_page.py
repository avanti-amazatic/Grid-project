from Pages.Basepage import BasePage
from Pages.Locators import *
import faker
f = faker.Faker()
from TestData.invetory_data_entry import *
from Pages.company_details_page import *


class HomePage(BasePage):

    def wait_for_home_page(self):
        self.wait_for_element(HomePageLocators.logout_button)

    def click_on_logout(self):
        self.driver.find_element(*HomePageLocators.logout_button).click()

    def click_on_add_company(self):
        self.driver.find_element(*HomePageLocators.add_company_button).click()

    def wait_for_create_company_page(self):
        self.wait_for_element(CreateCompanyLocators.company_name)

    def enter_company_name(self):
        company_test_data = f.company()
        self.driver.find_element(
            *CreateCompanyLocators.company_name).send_keys(company_test_data)
        return company_test_data

    def click_on_create_button(self):
        self.driver.find_element(*CreateCompanyLocators.create_button).click()

    def wait_for_table(self):
        self.wait_for_element(HomePageLocators.table_row_load)

    def check_table_entry(self):
        table = self.driver.find_element(*HomePageLocators.table)
        rows = table.find_elements(*HomePageLocators.table_rows)
        td = rows[0].find_elements(*HomePageLocators.table_content)
        company_name = td[1].text
        return company_name

    def pick_up_first_entry(self):
        table = self.driver.find_element(*HomePageLocators.table)
        rows = table.find_elements(*HomePageLocators.table_rows)
        td = rows[0].find_elements(*HomePageLocators.table_content)
        table_info = []
        table_info.extend((td[0], td[1], td[2], td[3]))
        td[0].click()

    def enter_new_url_and_inventory(self):
        self.driver.find_element(*CreateCompanyDetails.url).clear()
        new_url = CompanyDetailsPage(self.driver).enter_url()




