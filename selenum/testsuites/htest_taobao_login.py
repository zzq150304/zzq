 ##### from selenium import webdriver
from testsuites.basetestcase import BaseTestCase      ###### import unittest
from selenium.webdriver.common.keys import Keys
import time
import unittest
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(BaseTestCase):

    ##### def setUp(self):       # 主要是测试的前提准备工作
    #####     self.driver = webdriver.Chrome("../tools/chromedriver.exe")    # 尽量用相对路径
    #####     self.driver.implicitly_wait(5)
    #####     self.driver.get("https://www.baidu.com/")

    ##### def tearDown(self):    # 主要是测试结束后要做的操作。基本上都是关闭浏览器
    #####     time.sleep(3)
    #####     self.driver.quit()


    def test_baidu_search(self):      # 测试方法  必须用test 开头
                                      # 把测试逻辑代码   封装到 一个test 开头的方法里
        """
        # 1
        self.driver.find_element_by_id("kw").send_keys("selenium"+Keys.RETURN)
        time.sleep(2)
        assert "selenium" in self.driver.title
        """

        ## 2
        ## 声明 HomePage类 对象
        home_page = HomePage(self.driver)
        # home_page.open_url("https://www.baidu.com/")
        # 调用首页搜索功能
        home_page.search("selenium")


u"""每个测试用例脚本代码里 最后都加上这段代码   """
if __name__ == '__main__':                       # 告诉系统以 unittest的方式去执行      该文件运行时文件名就变成了main
    unittest.main()
                              #  去掉这句话。 有时pycharm 运行   并没有识别出要以 unittest的方式去执行
                           #  有这句话就可以在控制台运行（cmd 命令行）python 下编写的：测试用例脚本文件

               # 报错 importError/ModuleNotFoundError：No module named 'testsuites'  （就是没有找到unittest工具文件）
                              # --》去设：环境变量可解决这问题 ： 新建 PYTHONPATH   路径：D:\auto

                     # 该错误 说明你模块没导入成功，去看你的环境变量有没有问题

                       #cmd命令行能运行python文件 就是通过 看这个文件里有没有引用unittest这个工具类
                       #  因为这个路径/目录下有testsuites这个文件夹 ：该文件夹里有导过：import unittest模块
                                                 # python 环境运行它就是靠 unittest的方式来识别的
                                                 # 运行前先：先进入到测试用例脚本文件所在的目录
                                                 # python 文件名.py    来在cmd 中运行
