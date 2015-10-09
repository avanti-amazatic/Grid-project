import os
import unittest
from galenpy.galen_api import Galen
from galenpy.galen_report import TestReport, info_node, warn_node, error_node
from galenpy.galen_webdriver import GalenRemoteWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

PROJECT_NAME = 'galen-sample-py-tests'


class GalenTestBase(unittest.TestCase):
    def setUp(self):
        self.driver = GalenRemoteWebDriver("http://localhost:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_check_layout(self, test_name, specs, included_tags, excluded_tags):
        try:
            test_report = TestReport(test_name)
            check_layout_report = Galen().check_layout(self.driver,
                                                       os.path.join(os.path.dirname(__file__) + "/" + "specs/" + specs),
                                                       included_tags, excluded_tags)

            test_report.add_report_node(info_node("Running layout check for: " + test_name)
                                        .with_node(warn_node('this is just an example'))
                                        .with_node(error_node('to demonstrate reporting'))) \
                .add_layout_report_node("check " + specs, check_layout_report).finalize()
            if check_layout_report.errors > 0:
                raise AssertionError(
                    "Incorrect layout: " + test_name + " - Number of errors " + str(check_layout_report.errors))

        except Exception as e:
            raise e