#coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
from case_demo.unit_demo import UnitDemo
import os

#创建一个套件，可以认为是list，用于存放用例
# suite=unittest.TestSuite()

#添加1:基于用例名称添加
# suite.addTest(UnitDemo('test_02'))

# 4 指定类对象中的所有测试用例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitDemo))

# runner = unittest.TextTestRunner()
# runner.run(suite)

report_name='第一轮自动化测试报告'
report_title='UI自动化报告'
report_desc='测试报告描述详情'
#保存路径
report_path='./report_html/'
report_file=report_path+'report.html'
#判断report_path是否存在，如果不存在，就新增一个该路径
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass

#生成测试报告
with open(report_file,'wb') as report:
#添加测试用例到套件中
    suite=unittest.TestSuite()
# 4 指定类对象中的所有测试用例
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitDemo))
#创建HTMLTestRunner运行器
    reslut=HTMLTestRunner(stream=report,title=report_title,description=report_desc)
    reslut.run(suite)
