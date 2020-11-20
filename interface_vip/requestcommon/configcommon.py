# -*- coding: utf-8 -*-
# @Time     : 2020/07/01
# @Author   : daniel
# @File     : configcommon.py
# @Desc     : 基础配置读取
# @Version  : V1.0.0

import os
import configparser
import sys
# 主目录
base_path = os.getcwd()

path=sys.path[0]
# 测试运行配置
test_config_file = os.path.join(base_path, 'config', 'config.ini')
rc = configparser.ConfigParser()
rc.read(test_config_file, encoding='utf-8')
emailhost = rc.get('Email', 'host')
ports = rc.get('Email', 'port')
senders = rc.get('Email', 'sender')
password = rc.get('Email', 'pwd')
receivers = rc.get('Email', 'receiver')
msgto = rc.get('Email', 'msgto')


#测试用例目录
test_case_path = os.path.join(base_path, 'data')
# 运行日志
test_log_file = os.path.join(base_path, 'log', 'run.log')
# 日志等级
log_level = rc.get('log', 'log_level')
#unittest
unittest_path = rc.get('unittest', 'unittest_path')
#report
report_path = rc.get('report', 'report_path')
