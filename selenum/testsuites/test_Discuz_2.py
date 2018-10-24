from testsuites.basetestcase import BaseTestCase
from pageobjects.Dis_home_page import HomePage
from pageobjects.Dis_moren_page import MorenPage
from pageobjects.Dis_guanli_page import GuanliPage
from pageobjects.Dis_guanli_zz_page import GuanliZuan
from pageobjects.Dis_xinjian_page import XinjianPage
import unittest


class LunTan2(BaseTestCase):

    def test2(self):
        # 管理员用户登录
        home_page = HomePage(self.driver)
        home_page.login("admin","haotest")
        # 进入默认板块，删除帖子
        home_page.click_moren_bankuai()
        moren_page = MorenPage(self.driver)
        moren_page.delete_tiezi()
        # 进入版块管理(管理中心--论坛)    用的home_page页面的方法
        home_page.click_guanli()
        # 切换窗口
        home_page.goto_new_window()                # 直接调用的BasePage里的方法  没在Dis_home_page页面
        # 管理中心 输入密码登录
        guanli_zhuan_page = GuanliZuan(self.driver)
        guanli_zhuan_page.click_login("haotest")

        guanli_page =GuanliPage(self.driver)
        guanli_page.click_luntan()
        # 切进iframe
        guanli_page.cut_iframe("main")
        guanli_page.set_add_mokuai("dm1")
        # 管理员退出
        guanli_page.cut_main_html()                # 直接调用的BasePage里的方法  没在Dis_guanli_page页面
        guanli_page.quit_guanli()
        home_page.click_quit_guanli()
        # 普通用户登录
        home_page.login("admin","haotest")
        # 在新的版块下发帖
        home_page.click_xin_bankuai()

        xin_bankuan = XinjianPage(self.driver)
        xin_bankuan.fatie_xinbankuai("ha","gege")
        # 在新的版块下回帖
        xin_bankuan.huifu_xianjian_tiezi("word")


if __name__ =="__main__":
    unittest.main()

