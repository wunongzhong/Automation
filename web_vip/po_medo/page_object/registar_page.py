#coding=utf-8
from selenium import webdriver
from po_medo.base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from options.chrome_options import Options
#定义注册页

class registarPage(BasePage):
    '''
    registarPage的核心业务是注册流程的实现
    1.登陆关联的元素（element）获取
    2.基于元素实现的方式
    '''

    url = "http://39.98.138.157/shopxo/index.php?s=/index/user/reginfo.html"
    user =(By.NAME,"accounts")
    pwd = (By.NAME,"pwd")
    xuyi =(By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/label/span/i[2]')
    registar = (By.XPATH,"/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[4]/button")
    #断言元素

    #元素操作
    def input_user(self,txt):
        self.locator(self.user).send_keys(txt)
    def input_pwd(self,txt):
        self.locator(self.pwd).send_keys(txt)
    def click_xuyi(self):
        self.locator(self.xuyi).click()
    def click_registar(self):
        self.locator(self.registar).click()

    #断言方法

if __name__ == '__main__':
    # 调试
    options=Options().conf_option()
    driver = webdriver.Chrome(options=options)
    lp = registarPage(driver=driver,url=registarPage.url)
    lp.visit()
    lp.input_user('wunongzhong')
    lp.input_pwd('111111')
    lp.click_xuyi()
    lp.click_registar()
    lp.quit()
