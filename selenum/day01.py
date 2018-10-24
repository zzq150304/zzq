# 1

# from selenium import webdriver
#
# #### 第一步先new了一个对象 （意思是：脚本可以通过这个中间对象（webdriver）可以对浏览器进行操作控制）
# driver=webdriver.Chrome("./tools/chromedriver.exe")     # 可相对路径也可绝对路径（绝对路径写死了就不灵活）
# #### 用get方法来打开一个网页
# driver.get("http://www.python.org")
# #### assert断言的意思也就是做判断，看“Python”该文本有没有在打开的这个网页的title中。对，错如何？
# assert "Python" in driver.title
#




# 2

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.Chrome("./tools/chromedriver.exe")
# driver.get("http://www.yahoo.com")
# assert "Yahoo" in driver.title
# element=driver.find_element_by_name('p')
# element.send_keys('seleniumhq'+Keys.RETURN)
#driver.quit()






# 3

# import time
# from selenium import webdriver
#
# driver =webdriver.Chrome("./tools/chromedriver.exe")
# try:
#     driver.implicitly_wait(5)
#     driver.get("http://www.baidu.com")
#
#     driver.switch_to.window(driver.current_window_handle)
#
#     print("百度首页已经打开:",driver.title)
#
#     search_input=driver.find_element_by_id("kw")
#     search_input.send_keys("java")
#     search_input.submit()
#
#     nums=driver.find_element_by_class_name("nums")
#     print(nums.text)
#     driver.switch_to.window(driver.current_window_handle)           # 本来是
#
#     wait_seconds=5                         #                    format前是一个字符串  把$符替换成了\n
#     driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(nums.text.replace("\n","$"),wait_seconds))
#     time.sleep(wait_seconds)
#
# finally:
#     driver.quit()

