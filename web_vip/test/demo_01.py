#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# 封装显示等待
def dengdai(driver,path):
    qz = WebDriverWait(driver=driver,timeout=5,poll_frequency=0.5).until(
lambda el:driver.find_element_by_xpath(path),message='元素定位失败')
    return qz
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window() #窗体最大化
driver.get('https://music.163.com/')
dengdai(driver,'//*[text()="登录"]').click()
dengdai(driver,'//*[text()="选择其他登录模式"]').click()
dengdai(driver,'//*[text()="同意"]').click()
dengdai(driver,'//*[text()="QQ登录"]').click()
windows = driver.window_handles
#切换窗口
driver.switch_to.window(windows[1])
#通过id切换iframe
driver.switch_to.frame('ptlogin_iframe')
dengdai(driver,'//*[@id="qlogin_list"]/a/span[4]').click()
driver.switch_to.window(windows[0])
jiguo = dengdai(driver,'//*[text()="绑定手机号"]').text
# 判断是否登陆成功
assert '绑定手机号' == jiguo
driver.close()