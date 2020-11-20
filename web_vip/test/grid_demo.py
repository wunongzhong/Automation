#coding=utf-8

from selenium import webdriver
from time import sleep
ds = {'platform': 'Windows',
      'browserName': "chrome",
      'version': '84',
      'javascriptEnabled': True
      }
dr = webdriver.Remote('http://192.168.101.138:4445/wd/hub', desired_capabilities=ds)
dr.get("https://www.baidu.com")
dr.implicitly_wait(10)
dr.find_element_by_id('kw').send_keys('武大郎')
dr.find_element_by_id('su').click()
sleep(10)
dr.quit()