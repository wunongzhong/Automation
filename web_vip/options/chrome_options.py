#coding=utf-8
from selenium import webdriver

class Options:
    #浏览器初始化
    def conf_option(self):
        options=webdriver.ChromeOptions()
        #窗体最大化
        options.add_argument('start-maximized')
        #无头模式:启动浏览器进程，但是不会显示出来
        # options.add_argument('--headless')
        #去掉警告
        options.add_experimental_option('useAutomationExtension',False)
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        #去掉密码管理窗
        prefs={"":""}
        prefs["credentials_enable_service"]=False
        prefs["profile.password_manager_enabled"]=False
        options.add_experimental_option("prefs",prefs)

        # #去掉日志信息打印    适用命令行运行时需要添加如下：
        # options.add_argument('log_level=3')
        # #禁用显示“DevTools on ws：//”日志
        # options.add_experimental_option('excludeSwitches',['enable-logging'])
        return options