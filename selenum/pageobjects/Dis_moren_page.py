from pageobjects.base import BasePage
from selenium.webdriver.common.by import By


class MorenPage(BasePage):

    # (1) 定位要操作的元素
    moren_page_title_search_loc = (By.ID,"subject")
    moren_page_text_search_loc = (By.ID, "fastpostmessage")
    moren_page_button_search_loc = (By.CSS_SELECTOR,"#fastpostsubmit strong")

    # (2)退出 的元素定位
    moren_page_quit_search_loc = (By.LINK_TEXT, "退出")

    # (3)删除帖子 的元素定位
    moren_page_delete1_search_loc = (By.NAME, "moderate[]")
    moren_page_delete2_search_loc = (By.LINK_TEXT, "删除")
    moren_page_delete3_search_loc = (By.CSS_SELECTOR, "#modsubmit span")

    # (4)默认板块 的元素定位
    moren_page_moren_search_loc = (By.CSS_SELECTOR,".fl_icn img")



    def fatie(self,title,text):
        self.sendkeys(title,*self.moren_page_title_search_loc)
        self.sendkeys(text,*self.moren_page_text_search_loc)
        self.click(*self.moren_page_button_search_loc)

    def quit_moren(self):
        self.click(*self.moren_page_quit_search_loc)

    def delete_tiezi(self):
        self.click(*self.moren_page_delete1_search_loc)
        self.click(*self.moren_page_delete2_search_loc)
        self.click(*self.moren_page_delete3_search_loc)

    def click_morenbankuai(self,*loc):
        self.click(*self.moren_page_moren_search_loc)