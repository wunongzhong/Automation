#coding=utf-8
#导入ddt模块(第一步)
from ddt import ddt,data,unpack,file_data
import unittest
from selenium import webdriver
from options.chrome_options import Options
from time import sleep
#导入yaml模块
import yaml

#读取txt文件
# def read_txt():
#     list1=[]
#     file = open('ceshi_data.txt','r',encoding='utf-8')
#     for line in file.readlines():
#         list1.append(line.strip('\n').split(','))
#     file.close()
#     return list1

#读取yaml文件,但是实际运用无需读取操作，直接用@file_data（路径）
# def read_yaml():
#     file = open(r'../yaml_data/ceshi_data.yaml', 'r', encoding='utf-8')
#     # 解析yaml格式文件  Loader=yaml.FullLoader取消警告提示
#     value = yaml.load(file,Loader=yaml.FullLoader)
#     file.close()
#     #value=[{'url': 'http://www.baidu.com', 'txt': '后裔'}, {'url': 'http://www.baidu.com', 'txt': '诸葛亮'}]
#     return value


#声明ddt调用（第二步）
@ddt
class UnitDemo(unittest.TestCase):
    #传参调用data模块（第三步）
    # @data("后裔")
    # def test_01(self,txt):
    #     self.driver = webdriver.Chrome(options=Options().conf_option())
    #     self.driver.implicitly_wait(10)
    #     self.driver.get('http://www.baidu.com')
    #     self.driver.find_element_by_id('kw').send_keys(txt)
    #     self.driver.find_element_by_id('su').click()
    #     sleep(5)
    #     self.driver.quit()

    # @data(['http://www.baidu.com',"后裔"])
    # @unpack   #传入多个参数，需要导入unpack模块，数据加[]号，进行二次解析（第四步）
    # def test_02(self,url,txt):
    #     self.driver = webdriver.Chrome(options=Options().conf_option())
    #     self.driver.implicitly_wait(10)
    #     self.driver.get(url)
    #     self.driver.find_element_by_id('kw').send_keys(txt)
    #     self.driver.find_element_by_id('su').click()
    #     sleep(5)
    #     self.driver.quit()

    # @data(['http://www.baidu.com',"后裔"],['http://www.baidu.com',"诸葛亮"],['http://www.baidu.com',"黄月英"])
    # @unpack   #这条用例执行了三次
    # def test_03(self,url,txt):
    #     self.driver = webdriver.Chrome(options=Options().conf_option())
    #     self.driver.implicitly_wait(10)
    #     self.driver.get(url)
    #     self.driver.find_element_by_id('kw').send_keys(txt)
    #     self.driver.find_element_by_id('su').click()
    #     sleep(5)
    #     self.driver.quit()

    # @data(*read_txt())  #加*将外层[]号去掉（解析），读取txt文档进行操作
    # @unpack
    # def test_04(self,url,txt):
    #     self.driver = webdriver.Chrome(options=Options().conf_option())
    #     self.driver.implicitly_wait(10)
    #     self.driver.get(url)
    #     self.driver.find_element_by_id('kw').send_keys(txt)
    #     self.driver.find_element_by_id('su').click()
    #     sleep(5)
    #     self.driver.quit()

    @file_data('../yaml_data/ceshi_data.yaml')  # yaml模块
    def test_05(self, **kwargs):
        self.driver = webdriver.Chrome(options=Options().conf_option())
        self.driver.implicitly_wait(10)
        self.driver.get(kwargs['url'])
        self.driver.find_element_by_id('kw').send_keys(kwargs['txt'])
        self.driver.find_element_by_id('su').click()
        sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()