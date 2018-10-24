from pageobjects.Dis_home_page import HomePage
from pageobjects.Dis_moren_page import MorenPage
from pageobjects.Dis_huitie_page import HuitiePage
from testsuites.basetestcase import BaseTestCase
#import time
import unittest


class LunTan1(BaseTestCase):

    def test1(self):
        # 用户登录
        home_page = HomePage(self.driver)
        home_page.login("admin","haotest")
        # 默认板块发帖
        #time.sleep(2)
        moren_page = MorenPage(self.driver)
        moren_page.click_morenbankuai()
        moren_page.fatie("no","hello")
        # 默认板块回帖
        huitie_page = HuitiePage(self.driver)
        huitie_page.huitie("good")
        # 从默认板块  用户退出
        huitie_page.quit_huitie()


if __name__ =="__main__":
    unittest.main()


