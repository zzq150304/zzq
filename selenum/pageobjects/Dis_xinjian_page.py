from pageobjects.base import BasePage
from selenium.webdriver.common.by import By



class XinjianPage(BasePage):

    #(1)定位页面元素  发表帖子
    xinjian_page_title_search_loc = (By.CSS_SELECTOR,".px")
    xinjian_page_text_search_loc = (By.CSS_SELECTOR, ".pt")
    xinjian_page_submit_search_loc = (By.CSS_SELECTOR, "#fastpostsubmit strong")

    #(2)回复帖子 的元素定位
    xinjian_page_huifu_text_search_loc = (By.ID, "fastpostmessage")
    xinjian_page_huifu_submit_search_loc = (By.CSS_SELECTOR, "#fastpostsubmit strong")



    def fatie_xinbankuai(self,title,text):
        self.sendkeys(title,*self.xinjian_page_title_search_loc)
        self.sendkeys(text,*self.xinjian_page_text_search_loc)
        self.click(*self.xinjian_page_submit_search_loc)

    def huifu_xianjian_tiezi(self,text):
        self.sendkeys(text,*self.xinjian_page_huifu_text_search_loc)
        self.click(*self.xinjian_page_huifu_submit_search_loc)
