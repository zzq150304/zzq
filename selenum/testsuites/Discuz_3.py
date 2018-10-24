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

    # 帖子搜索
    time.sleep(3)
    driver.find_element_by_css_selector(".xg1").send_keys("no"+Keys.RETURN)
    driver.switch_to.window(driver.window_handles[1])
    abc1 = driver.find_element_by_css_selector(".xs3 font").click()
    driver.switch_to.window(driver.window_handles[2])
    abc2 = driver.find_element_by_id("thread_subject")

    if abc1.text == abc2.text:
        print("标题一致")
    else:
        print("打开帖子不正确")

    driver.find_element_by_link_text("退出").click()

finally:
    time.sleep(5)
    # driver.quit()