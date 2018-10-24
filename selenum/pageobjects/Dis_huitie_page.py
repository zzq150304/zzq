from selenium.webdriver.common.by import By
from pageobjects.base import BasePage


class HuitiePage(BasePage):

    # (1)定位元素
    huitie_page_text_search_loc = (By.ID,"fastpostmessage")
    huitie_page_button_search_loc = (By.ID, "fastpostsubmit")

    # (2)退出 的元素定位
    huitie_page_quit_search_loc = (By.ID,"退出")

    # (2)比对文章标题
    huitie_page_bidui_search_loc = (By.ID,"thread_subject")    # ??????????????


    def huitie(self,text):
        self.sendkeys(text,*self.huitie_page_text_search_loc)
        self.click(*self.huitie_page_button_search_loc)

    def quit_huitie(self):
        self.click(*self.huitie_page_quit_search_loc)

    def bidui(self,title):
        self