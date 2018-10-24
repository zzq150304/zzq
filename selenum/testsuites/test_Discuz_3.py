from testsuites.basetestcase import BaseTestCase
from pageobjects.Dis_home_page import HomePage
from selenium.webdriver.common.keys import Keys
import unittest


class Luntan2(BaseTestCase):
    def test_search_tiezi(self):
        home_page = HomePage(self.driver)
        home_page.login("admin","haotest")
        home_page.sendkeys("ha"+Keys.RETURN)


if __name__ =="__main__":
    unittest.main()