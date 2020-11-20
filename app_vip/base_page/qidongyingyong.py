#coding=utf-8
import yaml
import logging.config
from appium import webdriver

CON_LOG=r'../app_log/log_settings.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def app_qidongyingyong():
    stream=open(r'../yaml/settings.yaml','r')
    data=yaml.load(stream,Loader=yaml.FullLoader)

    cunchuxinxi={}
    cunchuxinxi['platformName']=data['platformName']

    cunchuxinxi['platformVersion']=data['platformVersion']
    cunchuxinxi['deviceName']=data['deviceName']

    cunchuxinxi['app']=data['app']
    cunchuxinxi['noReset']=data['noReset']

    cunchuxinxi['unicodeKeyboard']=data['unicodeKeyboard']
    cunchuxinxi['resetKeyboard']=data['resetKeyboard']

    cunchuxinxi['appPackage']=data['appPackage']
    cunchuxinxi['appActivity']=data['appActivity']
    stream.close()
    logging.info('==启动app中，请等待==')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', cunchuxinxi)

    driver.implicitly_wait(8)
    return driver