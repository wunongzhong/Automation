import unittest
from datetime import time, datetime
from HTMLTestRunner import HTMLTestRunner

from requestcommon.configcommon import unittest_path, report_path
from tools.sendemail import sendmail
from tools.log import logger
from BeautifulReport import BeautifulReport


class report:
    def toReport(self):
        logger.info("开始读取unittest测试核心目录")
        dir_path = unittest_path
        logger.info("开始使用discover到测试")
        try:
            discover = unittest.defaultTestLoader.discover(dir_path, pattern="*.py")
        except Exception as e:
            logger.error("加载unittest测试类路径失败，请查看问题！原因: s%", e)
        # 报告命名加上时间格式化
        logger.info("设置报告名称格式")
        time = datetime.now()
        now = time.strftime('%Y-%m-%d %H_%M_%S')
        # 报告绝对路径
        reportname = report_path + now
        reportpath= reportname + 'result.html'
        # 打开文件，写入测试结果
        # print(reportpath)
        logger.info("执行测试用例开始。。。。。。。。。。。。。")
        try:
            with open(reportpath, 'wb') as f:
                runner = HTMLTestRunner(stream=f, verbosity=2, title='接口ddt测试报告', description='用例执行详细信息')
                runner.run(discover)

            f.close()
            # result = BeautifulReport(discover)
            # result.report(description='用例执行详细信息', filename=reportname+"result")
        except Exception as e:
            logger.error("执行测试用例执行出错，请查看问题！原因: s%", e)
        logger.info("执行测试用例结束。。。。。。。。。。。。。")
        # sendmail().send_mail(reportpath)
