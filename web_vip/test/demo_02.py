#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# 封装显示等待
def dengdai(driver,path):
    qz = WebDriverWait(driver=driver,timeout=5,poll_frequency=0.5).until(
lambda el:driver.find_element_by_xpath(path),message='元素定位失败')
    return qz
user = "wu_766903532"
pwd = "ceshi123"
driver = webdriver.Chrome()
driver.implicitly_wait(5)#隐式等待
driver.maximize_window() #窗体最大化
driver.get('http://39.98.138.157/shopxo/')#打开网站
dengdai(driver,'//*[@class="menu-hd"]/a[2]').click()#点击注册
dengdai(driver,'//*[text()="用户名"]/../input').send_keys(user)#输入账号
dengdai(driver,'//*[text()="用户名"]/../../div[2]/div/input').send_keys(pwd)#输入密码
dengdai(driver,'//*[text()="用户名"]/../../div[3]/label').click()#点击同意
dengdai(driver,'//*[text()="用户名"]/../../div[4]/button').click()#点击注册
driver.quit()#关闭浏览器

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window() #窗体最大化
driver.get('http://39.98.138.157/shopxo/')
dengdai(driver,'//*[@class="menu-hd"]/a[1]').click()
dengdai(driver,'//*[@minlength="1"]').send_keys(user)
dengdai(driver,'//*[@placeholder="登录密码"]').send_keys(pwd)
dengdai(driver,'//*[@placeholder="登录密码"]/../../div[3]/button').click()
driver.quit()
