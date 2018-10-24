from pageobjects.base import BasePage
from selenium.webdriver.common.by import By


class GuanliZuan(BasePage):

    # (1) 输入框 的页面元素
    guanli_zhuan_pwd_search_loc = (By.CSS_SELECTOR,"#loginform .loginform .txt")
    guanli_zhuan_button_search_loc = (By.CSS_SELECTOR,".loginnofloat input")


    def click_login(self,pwd,*loc):
        self.sendkeys(pwd,*self.guanli_zhuan_pwd_search_loc)
        self.click(*self.guanli_zhuan_button_search_loc)

