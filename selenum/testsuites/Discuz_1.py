from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("../tools/chromedriver.exe")
try:
    ### login
    driver.implicitly_wait(5)
    driver.get("http://127.0.0.1/upload/forum.php")
    input1 = driver.find_element_by_id("ls_username")
    input1.send_keys("admin")
    input2 = driver.find_element_by_id("ls_password")
    input2.send_keys("haotest")
    driver.find_element_by_css_selector(".pn").click()

    ### 评论      ？？？？？？？ 下面用睡眠好？还是显式等待  检测时间太长  一般不都是10秒吗？？？？
    next_page = WebDriverWait(driver, 20).until(        ##   检测时间短(报错)：提高TimeoutException
        EC.element_to_be_clickable((By.LINK_TEXT, "默认版块")))
    next_page.click()
    # time.sleep(2)      ## 去掉等待（报错）：元素不附加到页面文档(过时的元素引用/stale element reference)
    # driver.find_element_by_link_text("默认版块").click()
    mo_input1 = driver.find_element_by_id("subject")
    mo_input1.send_keys("no")
    mo_input2 = driver.find_element_by_id("fastpostmessage")
    mo_input2.send_keys("hello......")
    driver.find_element_by_css_selector("#fastpostsubmit strong").click()

    hu_input = driver.find_element_by_id("fastpostmessage")
    hu_input.send_keys("hi...")
    driver.find_element_by_id("fastpostsubmit").click()
    time.sleep(3)
    driver.find_element_by_link_text("退出").click()

finally:
    time.sleep(5)
    # driver.quit()