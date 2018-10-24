# coding= utf-8
u"""   与业务无关的（页面）公共方法   """
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
import time
from framework.logger import Logger        # 导logger日志 + （定义到）用到每个def 方法里


# 生成/得到一个logger对象                            # 日志里就会输出:不同的（当前测试的）类名
logger = Logger(logger="BasePage").getlog()       # 想在下面的每个方法里调用  就要写在最外层
                                                  # （）里是固定写法：（logger=“调用它的类名”）
# 理解；当我们生成这个logger对象的时候 它就会自动去调用.__init__方法  把.__init__方法里定义的所有内容全部执行一遍
     #  然后我们就可以获取到--> 初始化好以后的logger对象



                           #   该类是所有页面的基类
class BasePage(object):    #   每一个页面的公共方法  ：所有页面的基类

    u"""
    （简写了很多selenium方法），重写了一些方法；增加了
     一些类方法，以后框架开发主要是扩展这个类。
    """

    u"""初始化方法（初始化某一个页面）"""
    def __init__(self,driver):
        self.driver = driver
                                                   # logger日志的输出语法：logger.info(" 正常执行，输出的文本内容 ")
                                                                         # logger.error(" 出异常 输出内容")
    u"""浏览器 后退 按钮"""
    def back(self):
        self.driver.back()
        logger.info(u"Click back on current page.     (检查：在当前的页面上按了一个“back”的文件)")


    u"""浏览器 前进 按钮"""
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.",u"当前页面成功前进到下一个页面")


    u"""关闭并停止浏览器服务"""
    def quit_Browser(self):
        self.driver.quit()
        logger.info("Click forward on current page.")


    u"""关闭当前页面"""
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except Exception as e:
            logger.error("Failed to quit the browser with %s"% e)


    u""" 打开一个 url 网页 """
    def open_url(self,url):
        self.driver.get(url)
        logger.info("Successfully open the specified web page")


    u""" 查找页面元素 """
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info(u"找到了页面元素----> ",loc)          #   ?????????????????????????????
        except:
            logger.error(u"%s 页面中未能找到 %s 元素"%(self,loc))    #   ??????????????????????


    u"""屏幕截图"""
    def get_windows_img(self):
        """
        在这里我们把file_path 这个参数写死，直接保存到我们项目根目录的一个文件夹.\screen_shots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screen_shots/'    # 或“/screen_shots/”
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name =file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info(u"Had take screenshots and save to folder : /screen_shots  已经添加了快照 并保存到了screen_shots目录下")
        except Exception as e:
            logger.error("Failed to take screen_shots! %s"% e ,u"截图失败")     #     失败的截图（截图失败）+ 异常消息%e


    u""" 输入 """
    def sendkeys(self,text,*loc):
        ele = self.find_element(*loc)
        ele.clear()
        try:
            ele.send_keys(text)
            logger.info("Successful input")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed Input with %s"% e)


    u"""清除文本框  """
    def clear(self,*loc):               ## 元组放最后  不能放字符串前面
        ele = self.find_element(*loc)
        try:
            ele.clear()
            logger.info("Successfully cleared")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to clear with %s"% e)
            ### print(#######)     也可以输出一些内容


    u"""点击元素"""
    def click(self,*loc):
        ele = self.find_element(*loc)         # 找到该元素再去点击 （相当于等待）
        try:     # 理解为：试运行
            ele.click()
            logger.info("The elemnet %s was clicked."% ele.text)
            # 引用模块找不见  报NameError 错误
        except NameError as e:                 # 理解为： 如果出现了任何的(错误)Exception 那就打印出自定义的提示内容和错误消息
            logger.error("Failed to click the element with %s"% e)


    u"""选择iframe
        切换html嵌套页面"""
    def cut_subpage_page(self,id):
        try:
            self.driver.switch_to.frame(id)
            logger.info("Successfully cut into nested HTML pages")
        except Exception as e:
            logger.error("Failed to enter the 'frame' page with %s"% e)


    u""" 从frame中切回主html页面 （退出iframe，回到上层）"""
    def cut_main_html(self):
        try:
            self.driver.switch_to.default_content()
            logger.info("Successfully return to the main HTML page")
        except Exception as e:
            logger.error("Failed return to the main HTML page with %s"% e)


    u"""跳转新的页面窗口"""
    def goto_new_window(self):
        try:
            WebDriverWait(self.driver,10).until(EC.number_of_windows_to_be(2))
            self.driver.switch_to.window(self.driver.window_handles[1])
            logger.info("Successfully go to new page window")
        except Exception as e:
            logger.error("Failed to go to new page window with %s"% e)


    u"""判断控件元素是否存在，返回boolean值"""
    def is_element_exists(self,*loc):
        flag = False
        try:
            self.find_element(*loc)
            flag = True
        except Exception as e:
            flag = False

        return flag


    u"""判断控件元素不存在，返回boolean值"""
    def is_not_element_exists(self,*loc):
        flag = False
        try:
            self.find_element(*loc)
            flag = False
        except Exception as e:
            flag = True

        return flag


    u"""判断web页面是不是加载完毕"""
    def is_page_load_complete(self):
        js = "return document.readyState"
        result = self.driver.execute_script(js)
        if result == "complete":
            return True
        else:
            return False


    """获得控件元素的文本信息"""
    def get_text(self,*loc):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(*loc))
        return self.find_element(*loc).text


    """  获取属性值  """
    def get_attribute(self,attrname,*loc):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(*loc))
        if self.is_element_exists(*loc):
            res = self.find_element(*loc).get_attribute(attrname)
            return res




"""
#########  调模块时  找不到该模块/包    会报NameException 错误

###  验证：os 帮助理解  针对get_windows_img（屏幕截图的函数方法）
file_path = os.path.dirname(os.path.abspath('.')) + '\\screen_shots\\'
#####  file_path = os.path.dirname(os.path.abspath('.')) + '/screen_shots/'
print(os.path.abspath('.'))                              # ---> D:\auto\pageobjects
print(os.path.dirname(os.path.abspath('.')))             # ---> D:\auto
print(file_path)                                          # ---> D:\auto\screen_shots\

rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))   #  该time 使用格式一定要会用
print(rq)                                                        #  201810111040

screen_name =file_path + rq + '.png'     #  输出的是它的全路径 （full path）
print(screen_name)                        #  D:\auto\screen_shots\201810111040.png
"""