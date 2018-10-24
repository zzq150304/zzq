u"""
浏览器引擎
                             frameword 下放的都是公共的类      只要是公共的类都继承自（最大的）---> object父类
  该类作用：   可以通过读取配置文件里所规定的浏览器的类型 ----》  来进行不同driver 的启动（运行）
                                           如选择（更改）运行 ---> 浏览器的驱动driver
"""

from selenium import webdriver
import os
from framework.logger import Logger
from configparser import ConfigParser
                             # ConfigParser类的作用 ：专门读取并解析 --->  .ini文件


logger = Logger(logger="BrowserEngin").getlog()   #  一说调日志  千万别忘：这句话（）


class BrowserEngin(object):
    # 得到浏览器驱动path 路径
    driver_dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_full_path = driver_dir + '\\tools\\chromedriver.exe'
          ## FireFox_.........
          ## ie_.........等其他


    def open_browser(self):
            # 创建一个引用对象
        config = ConfigParser()
            # 获取配置文件的全路径
        config_full_path = os.path.dirname(os.path.abspath('.')) + "\\config\\config.ini"
            # 通过该 read(一个参数是全路径) 方法 ---> 读取到.ini配置文件的内容
        config.read(config_full_path)


            #得到浏览器    得到它想切换(使用)的浏览器和URL      （在项目中会用不同的浏览器去测试一个系统）
        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser."% browser)
             #得到初始化打开的URL页面
        url = config.get("testServer","URL")
        logger.info("The test server url is: %s "% url)

                                               # 相当于给当前类定义/创建 了一个driver对象   且就在该方法里   它就可以调所有的东西  不需加self.
        if browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_full_path)                     # 这里的driver 前加不加self 都可以
            logger.info("Starting Chrome browser.")             #self.chrome_driver_full_path  加self 是因为这个变量定义在了该函数外在同类里的
        elif browser == "FireFox":
            driver=webdriver.Firefox(u"...没有下载对应的驱动driver.....")             # 这里的driver 前加不加self 都可以
            logger.info("No Firefox driver.")
        elif browser == "IE":
            driver=webdriver.Edge("...没有 IE=Edge 驱动文件...")                     # 这里的driver 前加不加self 都可以
            logger.info("No IE driver.")


        driver.get(url)                                                              # 这里的driver 前加不加self 都可以
        logger.info("open url:%s"% url)
        # driver.maximize_window()                                                    # 这里的driver 前加不加self 都可以
        # logger.info("Maximize the current window.")
        driver.implicitly_wait(10)                                                  # 这里的driver 前加不加self 都可以
        logger.info("Set implicitly wait 10 seconds.")
        return driver                                                              # 这里的driver 前加不加self 都可以


    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()                                            # 这里的driver 前必须加self.因为没在一个def 方法里，但在一个类里

