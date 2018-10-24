from selenium import webdriver
from selenium.webdriver.common.keys import Keys         #  键盘操作  7.4
from selenium.webdriver.common.action_chains import ActionChains      # 鼠标操作  7.2
import time



driver = webdriver.Chrome("./tools/chromedriver.exe")
try:
    driver.get("https://www.python.org/")
    time.sleep(3)
    menu = driver.find_element_by_link_text("Downloads")                       # 要找的菜单
    time.sleep(2)
    hidden_submenu = driver.find_element_by_link_text("All releases")          # 隐藏子菜单
    time.sleep(2)
    ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
        # .move_to_element() ：将鼠标移到那个元素对象上
        # .perform()  ： 将所有鼠标操作执行一遍

finally:
    time.sleep(5)
    driver.quit()