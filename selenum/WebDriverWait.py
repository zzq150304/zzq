from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC      # 预期条件
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("./tools/chromedriver.exe")

try:
    driver.implicitly_wait(5)
    driver.get("https://www.baidu.com/")
    a = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,"新闻")))             # 一般结合判断来用  if else
    a.click()
    print("当前页面是：",driver.title)

    time.sleep(3)
    driver.close()

finally:
    time.sleep(2)
    driver.quit()