from Pages.Basepage import BasePage
from Pages.Locators import *
import faker
f = faker.Faker()
from TestData.invetory_data_entry import *


class CompanyDetailsPage(BasePage):

    def wait_for_company_detail_page(self):
        self.wait_for_element(CreateCompanyDetails.url)

    def enter_url(self):
        self.driver.find_element(*CreateCompanyDetails.url).send_keys(
            f.domain_name())

    def enter_inventory(self):
        self.driver.find_element(*CreateCompanyDetails.inventory).send_keys(
            inventory_data)

    def click_on_save(self):
        self.driver.find_element(*CreateCompanyDetails.save_button).click()

    def wait_for_toast(self):
        self.wait_for_element(CreateCompanyDetails.toast)

    def go_back_on_accounts(self):
        self.driver.find_element(
            *CreateCompanyDetails.back_on_accounts).click()


