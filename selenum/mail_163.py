from selenium import webdriver
import time


# driver = webdriver.Chrome("./tools/chromedriver.exe")
# try:
#     driver.get("https://mail.163.com/")            ##  auto-id-1538969809072   是动态变化属性
#     time.sleep(5)                                  # nosuchelement  找不到页面元素的原因？
#     driver.switch_to.frame("x-URS-iframe")         # (1)元素未加载  --显式等待的作用        (2)浏览器切换（是不是操作的当前浏览器）
#     a=driver.find_element_by_name("email")         # (3)识别属性（动态变化属性）            (4)是否有iframe 嵌套页面
#     print(a.text)                                  # (5)alert弹出框                         (6)识别属性不是唯一
#
# finally:
#     driver.quit()



#####  alert 弹出框
# driver = webdriver.Chrome("./tools/chromedriver.exe")
# try:
#     driver.get("https://www.baidu.com/")
#     time.sleep(3)
#     driver.execute_script("window.alert('这是一个弹出框')")
#     time.sleep(3)
#     ###driver.switch_to.alert.accept()          # 点击确定的方法    .accept()
#     ###time.sleep(3)
#     driver.switch_to.alert.dismiss()          # 关闭弹出窗的方法  .dismiss()
#
#
# finally:
#     driver.quit()



##########    滚动   执行js代码
driver = webdriver.Chrome("./tools/chromedriver.exe")
try:
    driver.get("http://bbs.tianya.cn/")
    time.sleep(3)
    driver.execute_script("document.getElementById('bbs_left_nav').scrollTop=500")


finally:
    time.sleep(6)
    driver.quit()
