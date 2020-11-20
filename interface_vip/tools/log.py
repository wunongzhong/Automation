
# -*- coding: utf-8 -*-
# @Time     : 2020/07/05
# @Author   : daniel
# @File     : log.py
# @Desc     : 日志方法
# @Version  : V1.0.0

import logging
from logging import handlers
from requestcommon.configcommon import log_level, test_log_file

logger = logging.getLogger()

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("tornado").setLevel(logging.WARNING)
logging.getLogger("urllib").setLevel(logging.WARNING)
logging.getLogger("urllib2").setLevel(logging.WARNING)

# 设置日志等级
if log_level == str(0):
    logger.setLevel(logging.INFO)
elif log_level == str(1):
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

# 日志切割，最大100M，最多50个（创建文件输出）
file_handler = logging.handlers.RotatingFileHandler(test_log_file, mode='a', encoding='utf-8',
                                                    maxBytes=1024*1024*100, backupCount=50)
file_handler.setLevel(logging.DEBUG)

# 创建控制台输出handler
console_handler = logging.StreamHandler()

# 定义handler输出格式
formatter = logging.Formatter('[%(asctime)s] - [%(filename)s line:%(lineno)d] - %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# logger添加handler
logger.addHandler(file_handler)
logger.addHandler(console_handler)
