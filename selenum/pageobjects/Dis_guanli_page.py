from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class GuanliPage(BasePage):

    # (1)定位元素
    guanli_page_luntai_search_loc = (By.LINK_TEXT,"论坛")

    # (2)切换 iframe 嵌套页面 的元素定位
    # ？？？？？？？？？？？？？？、   main写死? 这是最好的方式吗

    #(3)"""退出iframe，回到上层"""

    # (4)创建新模块相关 的元素定位
    guanli_page_tianjia_search_loc = (By.LINK_TEXT,"添加新版块")
    guanli_page_input_search_loc = (By.NAME, "newforum[1][]")
    guanli_page_button_search_loc = (By.ID, "submit_editsubmit")

    # (5)退出管理页面 的元素定位
    guanli_page_tuichu_search_loc = (By.CSS_SELECTOR, ".uinfo a")



    def click_luntan(self,*loc):
        self.click(*self.guanli_page_luntai_search_loc)

    def cut_iframe(self,id):
        self.cut_subpage_page(id)

    def set_add_mokuai(self,name):
        self.click(*self.guanli_page_tianjia_search_loc)
        self.sendkeys(name,*self.guanli_page_input_search_loc)
        self.click(*self.guanli_page_button_search_loc)

    def quit_guanli(self):
        self.click(*self.guanli_page_tuichu_search_loc)

