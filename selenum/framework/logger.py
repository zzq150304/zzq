import logging
import time
import os


class Logger(object):
    def __init__(self,logger):    # 这为什么有一个参数 为了后期那个类调用它。把类名传进来
                                                      # 这因为这样，logger日志才能得到类名
        # 1.logger
        # 创建一个logger对象    注意：这有一个logger参数的（用来接收上面__init__里的logger参数）
        self.logger = logging.getLogger(logger)
        # 设置日志的输出的级别      大于等于你设置的日志级别--> 才会被输出
                                    # 从小---> 大  ：DEBUG 《  INFO  《  WARNING  《  ERROR
        self.logger.setLevel(logging.DEBUG)        #  DEBUG 下可以再 设置 比它级别高的 日志级别




        # 2.                                         #  调用日志级别时——————》语法：logging.+级别
        # Handler :控制日志输出在不同的地方          # 2 里没有logger 调用的方法
        # 创建一个 Handle ，用于写入日志   (1)放到文件里
        # 以当时的时间来作为文件名
        file_name = time.strftime("%Y%m%d %H%M",time.localtime(time.time()))
        # 日志输出/存放到哪？  利用os 模块----> 选定文件夹
        log_path = os.path.dirname(os.path.abspath('.')) + "\\logs\\"
        # 得到存放地址文件----> 所在的全（绝对）路径--------》来作为FileHandler()方法的参数
        full_path = log_path + file_name+'.log'         # file_name+'.log'是文件名     前面的log_path 是它的路径
        # 通过 FileHandler() 方法来创建handler 存放地   -----> 有一个绝对路径的参数
        file_handler = logging.FileHandler(full_path)
        # 再给他设置一个日记级别    因为在 DEBUG 下  只能比它的级别高，或相等  一般用INFO
        file_handler.setLevel(logging.INFO)

        # 再定义一个 （Handler定义成输出到控制台）
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)





        # 3
        # 3.Formatter: 定义handler 的输出格式                  #   固定格式写法（记住）
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
                        # asctime :将时间日期以字符串格式表示
                        # name: 当前类的类名
                        # levelname：日志级别名称
                        # message: 具体消息提示
        # 设置到 Handler上  定义输出地点的输出格式  ---》  用2Handler里的定义对象来引用
         # 用setFormatter()   方法
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)





        # 4
        # 把1,2,3 都连接起来    （2.3）连接了   但没连接1
         # 给logger 添加 handler  -------》 用addHandler()方法
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)




    # 通过定义这个方法获得logger 对象          # 上面的.__init__初始化方法   是定义logger
    def getlog(self):
        return self.logger         # 这个方法是  调用  上面的方法   给外面调它提供一个方法 总不能每次调用都实例化对象的
                                      #  这样 导它的时候     from framework.logger import Logger
                                             # 一调它里面的个getlog 方法 就会自动调用它的 .__init__方法
                                                    # 关键那句话：