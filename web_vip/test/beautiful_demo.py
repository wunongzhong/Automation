#coding=utf-8
#需要在用例那定义图片BeautifulReport源码有问题，截图报错
from BeautifulReport import BeautifulReport
import unittest
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
# root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')

#测试用例文件夹
test_dir = root_dir + "/case_demo"

#添加测试用例
discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern="unit_d*.py")
#设置报告名称
filename='test_report'
#设置测试报告路径
report_dir=root_dir + '/test'
#生成BR
bp = BeautifulReport(discover)
bp.report(description='百度UI测试',report_dir=report_dir,filename=filename)
