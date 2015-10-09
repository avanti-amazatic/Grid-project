import logging
logging.basicConfig(filename='/home/anand/Documents/TBN_Dashboard/log.log',
                    level=logging.INFO)

from re import sub
from decimal import Decimal

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app_login_code import BaseClass


class KpiValuesTest(BaseClass):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(
            'http://dev-tbn-dashboard.herokuapp.com/')
        self.admin_login()

    def test_kpi_values(self):
        """
        Test whether all the values appear or not in KPI section
        """
        wait = WebDriverWait(self.driver, 10)

        # Wait for 'Key performance index' card to load
        wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, '.inner-kpi-box')))

        # List of all the Kpi element's statistics
        kpi_list = self.driver.find_elements_by_css_selector(
            'md-grid-tile>figure>div')

        for kpis in kpi_list:
            # Separate the value of the particular kpi and percentage change
            kpi_value = kpis.text.split('\n')[0].strip()
            kpi_percentage_change = kpis.text.split('\n')[1].split(' ')[1].\
                strip()

            # assert value and percentage change is not blank
            self.assertIsNotNone(kpi_value)
            self.assertIsNotNone(kpi_percentage_change)

    def test_kpi_calculations(self):

        wait = WebDriverWait(self.driver, 10)

        # Wait for 'Key performance index' card to load
        wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, '.inner-kpi-box > md-grid-tile')))

        # Get the 'total earnings' figure
        total_earnings = self.driver.find_element_by_css_selector(
            'md-grid-tile.kpi:nth-child(3) > figure > div').text.split('\n')[0]\
            .strip()

        self.driver.find_element_by_css_selector(
            'md-grid-tile>figure>div')

        # Remove '$'sign and commas to perform arithmetic operations
        total_earnings = float(Decimal(sub(r'[^\d.]', '', total_earnings)))

        # Get the 'total impressions' figure
        total_impressions = self.driver.find_element_by_css_selector(
            'md-grid-tile.kpi:nth-child(4) > figure > div').text.split('\n')[0]\
            .replace(',', '')

        calculated_e_cpm = float(total_earnings) / (float(total_impressions) /
                                                    1000)
        calculated_e_cpm = '${:,.2f}'.format(float(calculated_e_cpm))
        # calculated_e_cpm = '$' + str(round(float(e_cpm), 2))

        displayed_e_cpm = self.driver.find_element_by_css_selector(
            'md-grid-tile.kpi:nth-child(8) > figure > div').text.split('\n')[0]\
            .strip()

        self.assertEqual(calculated_e_cpm, displayed_e_cpm)

        total_filled_impressions_figure = \
            self.driver.find_element_by_css_selector(
                'md-grid-tile.kpi:nth-child(5) > figure > div').text
        total_filled_impressions_split = total_filled_impressions_figure.split(
            '\n')
        filled_impressions = total_filled_impressions_split[0].replace(",", "")

        average_cpm = total_earnings / (float(filled_impressions)/1000)
        calculated_average_cpm = '$' + str(round(average_cpm, 2))

        displayed_average_cpm_figure = self.driver.find_element_by_css_selector(
            'md-grid-tile.kpi:nth-child(7) > figure:nth-child(1) > div:nth-child(1)').text
        displayed_average_cpm_split = displayed_average_cpm_figures.split('\n')
        displayed_average_cpm = displayed_average_cpm_split[0].strip()

        self.assertEqual(calculated_average_cpm, displayed_average_cpm)

        fill_rate = (float(filled_impressions) / float(total_impressions_text)) * 100
        calculated_fill_rate = str(round(fill_rate, 2)) + ' %'

        displayed_fill_rate_figures = self.driver.find_element_by_css_selector(
            'md-grid-tile.kpi:nth-child(9) > figure:nth-child(1) > '
            'div:nth-child(1)').text
        displayed_fill_rate_split = displayed_fill_rate_figures.split('\n')
        displayed_fill_rate = displayed_fill_rate_split[0].strip()

        self.assertEqual(calculated_fill_rate, displayed_fill_rate)

        displayed_page_views_figures = self.driver.find_element_by_css_selector(
            'md-grid-tile.kpi:nth-child(1) > figure:nth-child(1) > div:nth-child(1)').text
        displayed_page_views_split = displayed_page_views_figures.split('\n')
        page_views = displayed_page_views_split[0]
        kpi_list = self.driver.find_elements_by_css_selector(
            'md-grid-tile>figure>div')

        # Page Views is zero therefore calculations for RPM not possible
        # rpm = total_earnings / (float(page_views) / 1000)
        # calculated_rpm = '$' + str(round(rpm, 2))
        #
        # displayed_rpm_figure = self.driver.find_element_by_css_selector(
        #     'md-grid-tile.kpi:nth-child(6) > figure:nth-child(1) >
        #  div:nth-child(1)').text
        # displayed_rpm_split = displayed_rpm_figure.split('\n')
        # displayed_rpm = displayed_rpm_split[0].strip()
        #
        # self.assertEqual(calculated_rpm, displayed_rpm)


    def tearDown(self):
        self.driver.close()