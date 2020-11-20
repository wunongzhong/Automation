#coding=utf-8
import unittest
import os, datetime
from BeautifulReport import BeautifulReport

import sys
path='D:\\PyCharm\\untitled\\Automation\\app_vip\\'
sys.path.append(path)

#指定测试用例和测试报告的路径
test_dir = '../unit_test'
report_dir='../test_report'

if __name__ == '__main__':
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, 'test*.py', None)
    # 定义报告的文件格式
    now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    filename =report_dir+'/'+'测试报告' + str(now)
    BeautifulReport(discover).report(description='自动化测试报告', filename=filename,report_dir=report_dir)