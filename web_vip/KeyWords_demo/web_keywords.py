#coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains

from options.chrome_options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from log.log import Logger

log=Logger().get_logger()
#创建浏览器对象，通过反射机制
def open_brower(browser_type):
    #添加异常处理
    try:
        if browser_type == 'Chrome':
            log.info("chrome浏览器初始化，正在登陆中...")
            driver = webdriver.Chrome(options=Options().conf_option())
        else:
            log.info("非chrome开启，正在登陆中...")
            driver = getattr(webdriver,browser_type)()
    except:
        log.info("默认浏览器开启，正在登陆中...")
        driver = webdriver.Chrome()

    return driver

class WebUIKeys:

    #构造函数
    def __init__(self,browser_type):
        self.driver = open_brower(browser_type)

    #元素定位，反射机制
    def locator(self,**kwargs):
        try:
            return self.driver.find_element(getattr(By,kwargs['name'].upper()),kwargs['value'])
        except Exception as e:
            log.info(" '元素定位失败'信息：{}".format(e))

    #元素输入操作
    def input(self,**kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    #元素点击操作
    def click(self,**kwargs):
        self.locator(**kwargs).click()

    #浏览器关闭
    def quit(self):
        self.driver.quit()
    #截图
    def copy_img(self,imgpath):
        self.driver.get_screenshot_as_file(imgpath)

    #网页关闭
    def close(self):
        self.driver.close()

    #访问url
    def url(self,**kwargs):
        self.driver.get(kwargs['txt'])

    #强制等待
    def sleep(self,**kwargs):
        sleep(kwargs['txt'])

    #隐式等待
    def wait(self,**kwargs):
        self.driver.implicitly_wait(kwargs['txt'])

    #显示等待
    def show_wait(self,**kwargs):
        try:
            WebDriverWait(self.driver,5,0.5).until(lambda el:self.locator(**kwargs))
        except:
            log.info(" '元素定位失败'.")

    #悬停
    def xuanting(self,**kwargs):
        move = self.locator(**kwargs)
        ActionChains(self.driver).move_to_element(move).perform()

    #自定义断言
    def assert_text(self,**kwargs):
        reality = self.locator(**kwargs).text
        try:
            assert reality == kwargs['expect']
            log.info('断言成功')
            return True
        except:
            log.info('断言失败')
            return False
if __name__ == '__main__':
    a= getattr(By,'XPATH')
    print(a)