import time

import itertools

import datetime

from re import sub

from decimal import Decimal

from app_login_code import BaseClass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class LoginTest(BaseClass):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://dev-tbn-dashboard.herokuapp.com/')
        self.login_admin()

    def test_search_blog_clear_button(self):
        wait = WebDriverWait(self.driver, 10)

        # Assert search text box has 'All Blogs' initially
        search_placeholder_text = self.driver.find_element_by_css_selector('#input-0').get_attribute('placeholder')
        self.assertEqual(search_placeholder_text, 'All Blogs')

        # In search blog text box enter a letter to populate blogs
        self.driver.find_element_by_css_selector('#input-0').send_keys('s')

        # wait for the autocomplete list to load
        wait.until(EC.visibility_of_element_located(
            (By.ID, 'ul-0')))

        # Click on clear button in the 'search blog' textbox
        self.driver.find_element_by_css_selector('md-icon.ng-isolate-scope').click()

        # Check if the text box was successfully cleared
        self.assertEqual(search_placeholder_text, 'All Blogs')

        self.driver.find_element_by_id('input-0').send_keys('sisters')

        time.sleep(5)

        # Select sixsisters option from auto-complete list
        autocomplete_options = self.driver.find_element_by_id('ul-0')
        options_list = autocomplete_options.find_elements(By.TAG_NAME, 'li')
        for option in options_list:
            if option.text == "sixsistersstuff.com":
                option.click()
                time.sleep(0.5)
                break
            else:
                autocomplete_options.find_elements(By.TAG_NAME, 'li')

        # Assert loader animation
        loader = self.driver.find_element_by_css_selector('md-progress-linear.loader.md-default-theme')
        self.assertTrue(loader.is_displayed())

        # again click on clear button in search textbox
        self.driver.find_element_by_css_selector('md-icon.ng-isolate-scope').click()

        search_placeholder_text = self.driver.find_element_by_css_selector('#input-0').get_attribute('placeholder')
        self.assertEqual(search_placeholder_text, 'All Blogs')

        self.driver.find_element_by_id('input-0').send_keys('sisters')

        # wait for the autocomplete list to load
        wait.until(EC.visibility_of_element_located(
            (By.ID, 'ul-0')))

        # Select sixsisters option from auto-complete list
        autocomplete_options = self.driver.find_element_by_id('ul-0')
        all_options = autocomplete_options.find_elements(By.TAG_NAME, 'li')

        for single_option in all_options:
            if single_option.text == "sixsistersstuff.com":
                single_option.click()
                time.sleep(0.5)
                break

        self.driver.find_element_by_id('input-0').clear()
        self.assertEqual(search_placeholder_text, 'All Blogs')

    def test_filter(self):

        wait = WebDriverWait(self.driver, 10)

        # list
        date_range_css_selector = [29, 31, 32, 33]

        for css_selector in date_range_css_selector:

            # Click on 'Since' field to filter
            self.driver.find_element_by_css_selector('#select_value_label_5 > span').click()

            time.sleep(0.5)

            # Click on the desired option from the dropdown according to the list [eg. '29' is for 'custom date range']
            self.driver.find_element_by_css_selector('#select_option_{0} > div'.format(css_selector)).click()

            # Find loader and wait for it to disappear
            self.driver.find_element_by_css_selector('md-progress-linear.loader.md-default-theme')
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'md-progress-linear.loader.md-default-theme')))

            start_date = self.driver.find_element_by_id('input_16')
            end_date = self.driver.find_element_by_id('input_17')

            # assert that the 'start date' and 'end date' are disabled
            self.assertFalse(start_date.is_enabled())
            self.assertFalse(end_date.is_enabled())

            # Assert that the end date is the present date
            self.assertEqual(datetime.datetime.now().strftime('%B %-d, %Y'), end_date.get_attribute('value'))

            if css_selector == 29:
                expected_start_date  = (datetime.datetime.now() - datetime.timedelta(days=7))
                print(css_selector.strftime('%B %-d, %Y'))
                print(datetime.datetime.now().strftime('%B 1, %Y'))
                print(datetime.datetime.now().strftime('January 1, %Y'))

    def test_custom_date_range(self):
        wait = WebDriverWait(self.driver, 10)

        # Click on 'Since' filter type
        self.driver.find_element_by_css_selector('#select_value_label_5 > span').click()

        time.sleep(0.5)

        # Select custom date range from the filter
        self.driver.find_element_by_css_selector('#select_option_29 > div').click()

        # Find the loader and wait till the loader disappears
        self.driver.find_element_by_css_selector('md-progress-linear.loader.md-default-theme')
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'md-progress-linear.loader.md-default-theme')))

        # Click on start date label
        self.driver.find_element_by_xpath('//div[3]/div/md-card/md-card-content/div[2]/div/mdc-date-picker/'
                                          'md-input-container').click()

        # present_date = self.driver.find_element_by_id('input_16').text
        # datetime.datetime.now().month - present_date

        fortnight_from_now = (datetime.datetime.now() - datetime.timedelta(days=15))
        if datetime.datetime.now().month != fortnight_from_now.date().month:
            self.driver.find_element_by_css_selector('button.md-fab:nth-child(3)').click()
        d = str(fortnight_from_now.date().day)
        self.driver.find_element_by_link_text(d).click()
        self.driver.find_element_by_css_selector('button.md-primary:nth-child(2)').click()
        time.sleep(5)

    def test_plot(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'md-progress-linear.loader.md-default-theme')))
        since_dropdown = ["YESTERDAY", "WEEK_TO_DATE", "MONTH_TO_DATE", "YEAR_TO_DATE"]

        for css_selector in since_dropdown:

            # Click on 'Since' field to filter
            self.driver.find_element_by_css_selector('#select_value_label_5 > span').click()

            time.sleep(0.5)

            # Click on the desired option from the dropdown according to the list [eg. '29' is for 'custom date range']
            self.driver.find_element_by_css_selector('md-option[value = {0}] > div'.format(css_selector)).click()

            # Click on refresh data button
            self.driver.find_element_by_css_selector(
                '.ads-dashboard > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > md-card:nth-child(1) >'
                ' md-card-content:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)').click()

            # Find loader and wait for it to disappear
            self.driver.find_element_by_css_selector('md-progress-linear.loader.md-default-theme')
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'md-progress-linear.loader.md-default-theme')))

            if css_selector == "YESTERDAY":

                graph_start_date = self.driver.find_element_by_css_selector('.flot-x-axis > div:nth-child(1)').text
                calculated_start_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%b %d')

                self.assertEqual(graph_start_date, str(calculated_start_date))

            if css_selector == "WEEK_TO_DATE":

                graph_start_date = self.driver.find_element_by_css_selector('.flot-x-axis > div:nth-child(1)').text
                graph_end_date = self.driver.find_element_by_css_selector('.flot-x-axis > div:nth-last-child(1)').text
                calculated_start_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%b %d')
                calculated_end_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%b %d')

                self.assertEqual(graph_start_date, str(calculated_start_date))
                self.assertEqual(graph_end_date, str(calculated_end_date))

            if css_selector == "MONTH_TO_DATE":

                graph_start_date = self.driver.find_element_by_css_selector('.flot-x-axis > div:nth-child(1)').text
                graph_end_date = self.driver.find_element_by_css_selector('.flot-x-axis > div:nth-last-child(1)').text
                calculated_start_date = datetime.datetime.now().strftime('%b 01')
                calculated_end_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%b %d')

                self.assertEqual(graph_start_date, str(calculated_start_date))
                self.assertEqual(graph_end_date, str(calculated_end_date))

            if css_selector == "YEAR_TO_DATE":

                graph_start_date = self.driver.find_element_by_css_selector('.flot-x-axis > div:nth-child(1)').text
                calculated_start_date = datetime.datetime.now().strftime('Jan 01')

                print calculated_start_date

        self.driver.find_element_by_css_selector('smart-resource-loader.ng-isolate-scope:nth-child(1) > div:nth-child(1).text')

    def test_tool_tip(self):

        graph = self.driver.find_element_by_css_selector('canvas.flot-overlay:nth-child(3)')
        ActionChains(self.driver).move_to_element(graph).perform()
        time.sleep(1)
        tooltip_contents = self.driver.find_element_by_css_selector('.flotTip > div.daily-stats-tooltip > div')
        divs_list = tooltip_contents.find_elements(By.TAG_NAME, 'div')
        for divs in divs_list:
            amounts = divs.find_elements(By.TAG_NAME, 'span')
            for amount in amounts:
                print amount.text

                self.assertNotEqual(amount.text, '')

    def test_graph_links(self):
        wait = WebDriverWait(self.driver, 10)

        # Wait for the KPI grid list to load
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.inner-kpi-box')))

        for _ in range(2):
            # Since there are 10 elements in KPI ,loop will start from 1 till 10
            for selectors in range(1, 11):
                kpi_name = self.driver.find_element_by_css_selector(
                    'md-grid-tile.kpi:nth-child({0}) > figure:nth-child(1) > md-grid-tile-footer:nth-child(2)> '
                    'figcaption:nth-child(1) > span:nth-child(1)'.format(selectors)).text

                try:
                    # Check whether the particular kpi value is active or not, if it is active then go ahead click on it
                    graph_link = self.driver.find_element_by_css_selector(
                        'md-grid-tile.kpi:nth-child({0}) > figure:nth-child(1) > '
                        'div.dashboard-kpi.active'.format(selectors))
                    graph_link.click()
                    time.sleep(1)

                    # self.assertEqual(graph_link.value_of_css_property('border-style'), 'rgb(239, 239, 239)')

                    try:
                        # Check if the current graph is still visible
                        self.driver.find_element_by_css_selector(
                            'smart-resource-loader.ng-isolate-scope:nth-child(1) > div[ui-options*="{0}"]'.format(
                                kpi_name))
                        print 'Somethings wrong'
                    except NoSuchElementException:
                        pass

                except NoSuchElementException:
                    # If particular element is not active
                    inactive_graph = self.driver.find_element_by_css_selector(
                        'md-grid-tile.kpi:nth-child({0}) > figure:nth-child(1) > '
                        'div.dashboard-kpi'.format(selectors))
                    inactive_graph.click()
                    time.sleep(1)

                    # self.assertNotEqual(inactive_graph.value_of_css_property('border-color'), 'rgb(239, 239, 239)')

                    try:
                        self.driver.find_element_by_css_selector(
                            'smart-resource-loader.ng-isolate-scope:nth-child(1) > div[ui-options*="{0}"]'.format(
                                kpi_name))
                    except NoSuchElementException:
                        print kpi_name + ' graph did not get activated when clicked on it'

    def test_pie_chart(self):

        # Click on 'Revenue by Ad Type' pie chart to drill down
        self.driver.find_element_by_css_selector(
            '.ads-dashboard > div:nth-child(2) > div:nth-child(1) > md-card:nth-child(1) > md-card-content:nth-child(1)'
            ' > smart-resource-loader:nth-child(4) > div:nth-child(1) > canvas:nth-child(2)').click()

        time.sleep(1)

        # Find the label of Ad type details to assert drilled down page is displayed
        self.driver.find_element_by_css_selector(
            '.ads-dashboard > div:nth-child(2) > div:nth-child(1) > md-card:nth-child(1) > md-card-content:nth-child(1)'
            ' > smart-resource-loader:nth-child(4) > div[ui-options *= "Display Ads > Sovrn"]')

        # Click on 'Drill back' button
        self.driver.find_element_by_css_selector('button.md-fab.md-mini.md-primary.drill-back').click()

        time.sleep(1)

        try:
            self.driver.find_element_by_css_selector(
                '.ads-dashboard > div:nth-child(2) > div:nth-child(1) > md-card:nth-child(1) > '
                'md-card-content:nth-child(1)> smart-resource-loader:nth-child(4) > '
                'div[ui-options *= "Display Ads > Sovrn"]')
            raise ValueError('Something is wrong with the drill down back button')
        except NoSuchElementException:
            pass

        # Click on Ad Space impressions pie chart
        self.driver.find_element_by_css_selector(
            '.ads-dashboard > div:nth-child(2) > div:nth-child(2) > md-card:nth-child(1) > md-card-content:nth-child(1)'
            ' > smart-resource-loader:nth-child(4) > div:nth-child(1) > canvas:nth-child(2)').click()
        time.sleep(1)

        # Find element on a drilled down page
        self.driver.find_element_by_css_selector(
            '.ads-dashboard > div:nth-child(2) > div:nth-child(2) > md-card:nth-child(1) > md-card-content:nth-child(1)'
            ' > smart-resource-loader:nth-child(4) > div[ui-options *= "Medium Rectangle > BTF"]')

        # Click on 'Drill back' button
        self.driver.find_element_by_css_selector('.ads-dashboard > div:nth-child(2) > div:nth-child(2) > '
                                                 'md-card:nth-child(1) > md-card-content:nth-child(1) >'
                                                 ' smart-resource-loader:nth-child(4) > button:nth-child(2)').click()
        self.driver.find_element_by_css_selector(
            '.ads-dashboard > div:nth-child(2) > div:nth-child(2) > md-card:nth-child(1) > md-card-content:nth-child(1)'
            ' > smart-resource-loader:nth-child(4) > div[ui-options *= "Leaderboard"]')

    def test_ad_graph_name_scale(self):

        wait = WebDriverWait(self.driver, 10)

        # Wait for the KPI grid list to load
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.inner-kpi-box')))

        for _ in range(2):
            # Since there are 10 elements in KPI ,loop will start from 1 till 10
            for selectors in range(1, 11):
                kpi_name = self.driver.find_element_by_css_selector(
                    'md-grid-tile.kpi:nth-child({0}) > figure:nth-child(1) > md-grid-tile-footer:nth-child(2)> '
                    'figcaption:nth-child(1) > span:nth-child(1)'.format(selectors)).text

                # Check whether the particular kpi value is active or not, if it is active then go ahead click on it
                try:
                    self.driver.find_element_by_css_selector(
                        'md-grid-tile.kpi:nth-child({0}) > figure:nth-child(1) > '
                        'div.dashboard-kpi.active'.format(selectors))
                    active = True
                except NoSuchElementException:
                    active = False

                graph_link = self.driver.find_element_by_css_selector(
                    'md-grid-tile.kpi:nth-child({0}) > figure:nth-child(1) > '
                    'div'.format(selectors))

                graph_link.click()
                time.sleep(4)

                graph_info = self.driver.find_element_by_css_selector(
                    'div.legend:nth-child(4) > table:nth-child(2) > tbody:nth-child(1)')
                no_of_info = graph_info.find_elements_by_tag_name('tr')
                name_on_graph = []

                for x in range(1, len(no_of_info)+1):
                    name_on_graph.append(self.driver.find_element_by_css_selector(
                        'div.legend:nth-child(4) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child({0}) '
                        '> td:nth-child(2)'.format(x)).text.split('(')[0].strip())
                if active:
                    self.assertTrue(kpi_name not in name_on_graph)
                else:
                    self.assertTrue(kpi_name in name_on_graph)

    def test_pie_chat_tooltip(self):

        wait = WebDriverWait(self.driver, 10)

        # wait till the pie chart loads
        ad_image = wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, '.ads-dashboard > div:nth-child(2) > div:nth-child(1) > md-card:nth-child(1) >'
                             ' md-card-content:nth-child(1) > smart-resource-loader:nth-child(4) > div:nth-child(1)')))

        ActionChains(self.driver).move_to_element(ad_image).perform()
        time.sleep(10)

        blue_ad_image = self.driver.find_element_by_css_selector(
            '.ads-dashboard > div:nth-child(2) > div:nth-child(1) > md-card:nth-child(1) > md-card-content:nth-child(1)'
            ' > smart-resource-loader:nth-child(4) > div')
        ActionChains(self.driver).move_to_element_with_offset(blue_ad_image, 100, 100).perform()
        time.sleep(3)
        # self.driver.find_element_by_css_selector('')
        # [style *= "rgb(239, 76, 53)"]

    def test_filter_combination(self):
        wait = WebDriverWait(self.driver, 10)

        for types in range(28, 32):
            self.driver.find_element_by_css_selector('#select_value_label_4 > span:nth-child(2)').click()
            time.sleep(0.5)
            self.driver.find_element_by_id('select_option_{0}'.format(types)).click()
            for type2 in range(32, 38):
                self.driver.find_element_by_css_selector('#select_value_label_5 > span:nth-child(2)').click()
                time.sleep(0.5)
                self.driver.find_element_by_id('select_option_{0}'.format(type2)).click()

                refresh_button = self.driver.find_element_by_css_selector(
                    '.ads-dashboard > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > md-card:nth-child(1) >'
                    ' md-card-content:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)')
                data = self.driver.find_element_by_css_selector('smart-resource-loader.ng-isolate-scope:nth-child(1) > div:nth-child(1)')

                ActionChains(self.driver).move_to_element(refresh_button).click().perform()
                data = data.get_attribute("ui-options")
                loader = self.driver.find_element_by_css_selector('md-progress-linear.loader.md-default-theme')
                wait.until(EC.invisibility_of_element_located((
                    By.CSS_SELECTOR, 'md-progress-linear.loader.md-default-theme')))

    def test_kpi_combinations(self):
        kpi_list = self.driver.find_elements_by_tag_name('md-grid-tile')

        for active_kpi in kpi_list:
            try:
                active_kpi.find_element_by_css_selector('div.dashboard-kpi.active').click()
            except NoSuchElementException:
                pass

        # for L in range(1, len(kpi_list)+1):
            # for subset in itertools.combinations(kpi_list, L):
                # for K in range(1, len(subset)+1):
                # for x in kpi_list():

    def tearDown(self):
        self.driver.close()
