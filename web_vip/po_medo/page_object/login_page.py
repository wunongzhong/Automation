#coding=utf-8
from selenium import webdriver
from po_medo.base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from options.chrome_options import Options
#定义登陆页

class loginPage(BasePage):
    '''
    loginPage的核心业务是登陆流程的实现
    1.登陆关联的元素（element）获取
    2.基于元素实现的方式
    '''

    url = "http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html"
    user =(By.NAME,"accounts")
    pwd = (By.NAME,"pwd")
    login = (By.XPATH,"/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button")

    #元素操作
    def input_user(self,txt):
        self.locator(self.user).send_keys(txt)
    def input_pwd(self,txt):
        self.locator(self.pwd).send_keys(txt)
    def click_login(self):
        self.locator(self.login).click()

    #登陆方法
    def logining(self,**data):
        lp = loginPage(driver=driver, url=loginPage.url)
        lp.visit()
        lp.input_user(data['user'])
        lp.input_pwd(data['pwd'])
        lp.click_login()

if __name__ == '__main__':
    #调试
    options=Options().conf_option()
    ds = {'platform': 'Windows',
          'browserName': "chrome",
          'version': '84',
          'javascriptEnabled': True
          }
    driver = webdriver.Remote('http://192.168.101.138:4445/wd/hub', desired_capabilities=ds,options=options)
    # driver = webdriver.Chrome(options=options)
    # 页面对象在实例化的时候都需要传递一个driver，不同的driver会执行不同的操作
    lp = loginPage(driver=driver,url=loginPage.url)
    lp.visit()
    lp.input_user('wunongzhong')
    lp.input_pwd('111111')
    lp.click_login()
    lp.quit()


