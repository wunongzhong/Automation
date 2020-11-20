#coding=utf-8
import logging

#创建一个log
def log():
    Logger = logging.getLogger('Logger')
    #创建总日志等级
    Logger.setLevel(logging.DEBUG)
    if not Logger.handlers:
        #创建文件输出格式
        fmt = logging.Formatter(fmt='[%(filename)s]:%(asctime)s - %(levelname)s - %(message)s')

        #创建一个平台输出方法
        pt = logging.StreamHandler()
        pt.setLevel(logging.DEBUG)
        pt.setFormatter(fmt)
        #加入控制台
        Logger.addHandler(pt)

        #创建一个文件输出方法
        wj = logging.FileHandler('app_log.txt', mode='a')
        wj.setLevel(logging.INFO)
        wj.setFormatter(fmt)
        #写入文件
        Logger.addHandler(wj)
    return Logger