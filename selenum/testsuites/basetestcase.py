# coding = utf-8
from selenium import webdriver
import unittest
import time
from framework.browser_engine import BrowserEngin


class BaseTestCase(unittest.TestCase):        # TestCase是基类（父类）

    def setUp(self):       # 主要是测试的前提准备工作
        browser = BrowserEngin()
        self.driver = browser.open_browser()         # 尽量保证所有的浏览器共用同一个driver

        # self.driver = webdriver.Chrome("../tools/chromedriver.exe")  # 尽量用相对路径
        # self.driver.implicitly_wait(5)
        ##########  self.driver.get("https://www.baidu.com/")

    def tearDown(self):    # 主要是测试结束后要做的操作。基本上都是关闭浏览器
        time.sleep(3)
        self.driver.quit()