#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
# 封装显示等待
def dengdai(driver,path):
    sleep(0.5)
    qz = WebDriverWait(driver=driver,timeout=5,poll_frequency=0.5).until(
lambda el:driver.find_element_by_xpath(path),message='元素定位失败')
    return qz

user = "wu_766903532"
pwd = "ceshi123"
class shipping():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window() #窗体最大化
        self.driver.get('http://39.98.138.157/shopxo/')
    def login(self):
        dengdai(self.driver,'//*[@class="menu-hd"]/a[1]').click()
        dengdai(self.driver,'//*[@minlength="1"]').send_keys(user)
        dengdai(self.driver,'//*[@placeholder="登录密码"]').send_keys(pwd)
        dengdai(self.driver,'//*[@placeholder="登录密码"]/../../div[3]/button').click()
        sleep(3)
    def chaxun(self):
        dengdai(self.driver,'//*[@id="search-input"]').send_keys("手机")
        dengdai(self.driver, '//*[@id="ai-topsearch"]').click()
    def xuanzhe(self):
        dengdai(self.driver, '//*[contains(text(),"苹果")]').click()
        windows = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(windows[1])
        dengdai(self.driver, '//*[@data-value="套餐一"]').click()
        dengdai(self.driver, '//*[@data-value="银色"]').click()
        dengdai(self.driver, '//*[@data-value="64G"]').click()
        dengdai(self.driver, '//*[@id="text_box"]').clear()
        dengdai(self.driver, '//*[@id="text_box"]').send_keys("10")
        dengdai(self.driver, '//*[contains(text(),"加入购物车")]').click()
        sleep(3)
    def gouwucheyanzheng(self):
        dengdai(self.driver, '//*[text()="购物车"]').click()
        jieguo= dengdai(self.driver, '//*[contains(text(),"苹果")]').text
        text="苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G"
        shuliang = dengdai(self.driver, '//input[@class="am-form-field" and @type="number"]')
        sl = int(shuliang.get_attribute("value"))
        assert jieguo==text and sl==10
        sleep(1)
        self.driver.quit()

if __name__ == '__main__':
    lc = shipping()
    lc.login()
    lc.chaxun()
    lc.xuanzhe()
    lc.gouwucheyanzheng()