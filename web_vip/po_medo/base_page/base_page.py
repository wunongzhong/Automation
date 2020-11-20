#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#定义基类:提供各个po对象来调用公共类
class BasePage(object):
    #定义构造函数,所有内容都是基于driver操作，所有需要传driver
    #定义构造函数，每一个面都有url，定义好url，在类中都能调用
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    #元素定位
    def locator(self,loc):
        return self.driver.find_element(*loc)

    #访问指定的url
    def visit(self):
        self.driver.get(self.url)

    #关闭浏览器
    def quit(self):
        sleep(5)
        self.driver.quit()