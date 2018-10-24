####   执行所有测试用例的一个入口文件  ####     unittest提供的一些类和方法  来对多个测试用例脚本的批量运行
# coding = utf-8
import unittest
import time
import os
import HTMLTestRunner


test_dir = './'                             # ./当前目录  运行以test开头... .py结尾的所有文件
suite = unittest.TestLoader().discover(test_dir,pattern='test*.py')


# """生成HTML报告文件"""
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
file_name = time.strftime('%Y%m%d %H%M%S',time.localtime(time.time()))
html_file_full_path = report_path + file_name + "_result.html"
fp = open(html_file_full_path,'wb')



if __name__ == "__main__":
    #执行用例
    # 这段代码只会创建输出日志
    # runner = unittest.TextTestRunner()                # HTMLTestRunner 类里包含了批量运行的  .run方法
    # 这段代码即会输出报告 有会输出日志
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"自动化测试报告，测试如下",description=u"用例测试情况如下")
    runner.run(suite)
    # fp.close()
                                              #  每一个.py文件都有一个隐含的属性：__name__  该属性默认值=文件名
                                              #  但当你单机运行的时候   该文件名就会自动变成 main
