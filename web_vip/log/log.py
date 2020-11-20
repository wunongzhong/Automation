#coding=utf-8
import logging

class Logger:
    def get_logger(self):
        # 第一步，创建一个logger
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        #去除控制台输出重复
        if not logger.handlers:
            fmt = logging.Formatter(fmt='[%(filename)s]:%(asctime)s - %(levelname)s - %(message)s')
            #创建控制台输出
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)
            sh.setFormatter(fmt)
            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler('../web_log.txt', mode='a')  # open的打开模式这里可以进行参考
            fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
            fh.setFormatter(fmt)
            # 加入控制台
            logger.addHandler(fh)
            logger.addHandler(sh)
        return logger
log = Logger().get_logger()
# # 第一步，创建一个logger
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)  # Log等级总开关  此时是INFO
#
# # 第二步，创建一个handler，用于写入日志文件
# logfile = './app_log.txt'
# fh = logging.FileHandler(logfile, mode='a')  # open的打开模式这里可以进行参考
# fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
#
# # 第三步，再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关
#
# # 第四步，定义handler的输出格式（时间，文件，行数，错误级别，错误提示）
# formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # 第五步，将logger添加到handler里面
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# # 日志级别
# logger.debug('这是 logger debug message')
# logger.info('这是 logger info message')
# logger.warning('这是 logger warning message')
# logger.error('这是 logger error message')
# logger.critical('这是 logger critical message')
# #
# DEBUG：详细的信息,通常只出现在诊断问题上
# INFO：确认一切按预期运行
# WARNING（默认）：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
# ERROR：更严重的问题,软件没能执行一些功能
# CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行