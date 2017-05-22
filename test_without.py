import unittest
from selenium import webdriver
import sys
import os

#import logging
#logging.basicConfig(level=logging.DEBUG)


class WithoutTestCase(unittest.TestCase):

    app_address = os.environ['APP_ADDRESS']
    hub_address = os.environ['HUB_ADDRESS']
    desired_capabilities = {
        'platform': os.environ['TEST_PLATFORM'],
        'browserName': os.environ['TEST_BROWSER'],
    }

    def setUp(self):
        self.driver = webdriver.Remote(self.hub_address,
                                       self.desired_capabilities)
        self.driver.get(self.app_address)

    def tearDown(self):
        self.driver.quit()

    def test_inspect_introduction(self):
        self.driver.find_element_by_link_text('Introduction').click()
        a = self.driver.find_element_by_id('welcome')
        self.assertTrue(a.is_displayed())

    def test_inspect_installationt(self):
        self.driver.find_element_by_link_text('Introduction').click()
        a = self.driver.find_element_by_id('introduction')
        self.assertTrue(a.is_displayed())


if __name__ == '__main__':
    unittest.main()
