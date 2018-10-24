from selenium import webdriver

# (1)  获取所有超链接
# driver = webdriver.Chrome("./tools/chromedriver.exe")
# driver.get("https://www.baidu.com/")
# assert "百度一下，你就知道" in driver.title
#
# links=driver.find_elements_by_tag_name("a")
#                              # 返回的是一个页面元素的集合（列表）    列表只能是遍历输出
#                             # 类类型的地理位置      或可以通过它本身的属性（方法）来输出（.text）
#                             #  print(nums.text)
# print("共找到a标签",len(links),"个")
# for ele in links:        # 遍历该列表里的每一个元素。
#     print(ele.text)      #  不能直接输出元素：只能输出该元素的某些属性
#                                             # get_attribute   该方法是获取元素的属性值
# driver.quit()




# (2)练习：find_element_by_link_text 和 find_element_by_partial_link_text 和 .find_element_by_css_selector
# driver = webdriver.Chrome("./tools/chromedriver.exe")
# driver.get("https://www.baidu.com/")
# assert "百度一下，你就知道" in driver.title
#
# news=driver.find_element_by_link_text("新闻").click()
# long_link=driver.find_element_by_partial_link_text("彭丽媛在联合国")
# #####  或 long_link=driver.find_element_by_css_selector("彭丽媛在联合国")
# print(long_link.text)
#
# driver.quit()





# (3)获取所有邮箱(有待更改正则)查找不准确
# import re                      #导入正则模块   就可以用正则表达式

# driver = webdriver.Chrome("./tools/chromedriver.exe")
# driver.get("http://home.baidu.com/home/index/contact_us")
# assert "联系百度" in driver.title
#
# emails=driver.find_elements_by_css_selector(".mail-content-text")
# print("email的个数：",len(emails))
# for link in emails:
#     print(link.text)
# driver.quit()

# 3 另一种解法
import re

driver = webdriver.Chrome("./tools/chromedriver.exe")
driver.maximize_window()      #页面最大化
driver.implicitly_wait(5)     # 贯穿从它开始到最后  （每次查找超过5秒报超时错误）

driver.get("http://home.baidu.com/contact.html")
# 得到页面源代码
doc = driver.page_source              # 返回的doc 也是str  可直接print（doc）输出
emails = re.findall(r'[\w]+@[\w\.-]+', doc)  # 利用正则，找出 xxx@xxx.xxx 的字段，保存到emails列表
# 循环打印匹配的邮箱                      #  r' 意思是声明一下  后面的代码内容是  正则表达式
for email in emails:
    print(email)                 # emils 用正则匹配到的 返回的是字符串str  可直接print（变量名）输出
