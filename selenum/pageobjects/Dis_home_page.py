from pageobjects.base import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    # (1) 先在页面定位要操作的元素
    home_page_input1_search_loc = (By.ID,"ls_username")
    home_page_input2_search_loc = (By.ID, "ls_password")
    home_page_button_search_loc = (By.CSS_SELECTOR,".pn")

    # (2)默认板块元素的定位
    moren_search_loc = (By.LINK_TEXT,"默认版块")

    # (3)新建的板块 的元素定位
    xin_search_loc = (By.CSS_SELECTOR,".fl_row h2 a")


    # (4)管理中心 的元素定位
    guanli_search_loc = (By.LINK_TEXT,"管理中心")


    # (6)管理员退出 的元素定位
    quit_search_loc = (By.LINK_TEXT,"退出")

    # (7)帖子搜索 的元素定位
    home_page_tiezi_search_loc = (By.CSS_SELECTOR,".xg1")



    def login(self,user,pwd):
        self.sendkeys(user,*self.home_page_input1_search_loc)
        self.sendkeys(pwd,*self.home_page_input2_search_loc)
        self.click(*self.home_page_button_search_loc)

    def click_moren_bankuai(self,*loc):
        self.click(*self.moren_search_loc)

    def click_xin_bankuai(self,*loc):
        self.click(*self.xin_search_loc)

    def click_guanli(self,*loc):
        self.click(*self.guanli_search_loc)

    def click_quit_guanli(self,*loc):
        self.click(*self.quit_search_loc)




