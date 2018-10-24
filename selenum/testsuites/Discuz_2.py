from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver.exe")
try:
    ### login
    driver.implicitly_wait(5)
    driver.get("http://127.0.0.1/upload/forum.php")
    input1 = driver.find_element_by_id("ls_username")
    input1.send_keys("admin")
    input2 = driver.find_element_by_id("ls_password")
    input2.send_keys("haotest")
    driver.find_element_by_css_selector(".pn").click()

    #### 删除帖子
    time.sleep(2)
    driver.find_element_by_link_text("默认版块").click()
    time.sleep(1)
    driver.find_element_by_name("moderate[]").click()
    time.sleep(1)
    driver.find_element_by_link_text("删除").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#modsubmit span").click()

    #### 进入版块管理
    time.sleep(2)
    driver.find_element_by_link_text("管理中心").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)                                                                       ###########
    driver.find_element_by_name("admin_password").send_keys("haotest"+Keys.RETURN)   ###########
    time.sleep(3)
    driver.find_element_by_link_text("论坛").click()
    time.sleep(3)
    driver.switch_to.frame("main")                                                            # 有iframe嵌套
    driver.find_element_by_link_text("添加新版块").click()
    time.sleep(1)
    driver.find_element_by_name("newforum[1][]").send_keys("dm1")   # ?????   .clear
    time.sleep(1)
    driver.find_element_by_id("submit_editsubmit").click()
    time.sleep(3)
    driver.switch_to.default_content()                  #  从frame中切回主文档
    time.sleep(2)
    driver.find_element_by_link_text("退出").click()
    time.sleep(3)
    driver.find_element_by_link_text("退出").click()

    # 再次login
    time.sleep(2)
    input3 = driver.find_element_by_id("ls_username")
    input3.send_keys("admin")
    input4 = driver.find_element_by_id("ls_password")
    input4.send_keys("haotest")
    driver.find_element_by_css_selector(".pn").click()

    #### 新版块发帖子
    time.sleep(2)
    driver.find_element_by_css_selector(".fl_row h2 a").click()                         # 超链接点击不能用submit  只能用click
    time.sleep(2)                                                                         # 按钮点击可以用submit
    driver.find_element_by_css_selector(".px").send_keys("mo")
    driver.find_element_by_css_selector(".pt").send_keys("hello......")
    driver.find_element_by_css_selector("#fastpostsubmit strong").submit()
    time.sleep(3)
    driver.find_element_by_id("fastpostmessage").send_keys("aaaaaa")
    driver.find_element_by_css_selector("#fastpostsubmit strong").submit()


finally:
    time.sleep(5)
    # driver.quit()