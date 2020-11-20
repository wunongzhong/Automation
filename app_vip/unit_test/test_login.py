#coding=utf-8
import unittest
from base_page.qidongyingyong import app_qidongyingyong
from page_object.login_page import denglu
import logging
from  time import sleep

class kaishijieshu(unittest.TestCase):

    def setUp(self):
        logging.info('======开始setUp=========')
        self.driver=app_qidongyingyong()


    def tearDown(self):
        logging.info('======结束tearDown=====')
        sleep(3)
        self.driver.close_app()

    def test_denglu_cm01(self):
        logging.info('=========开始登录cemaxueyuan01============')
        l= denglu(self.driver)
        l.denglu_kaishi('cemaxueyuan01','cema123456')


    def test_denglu_cm02(self):
        logging.info('==========开始登录cemaxueyuan02========')
        l=denglu(self.driver)
        l.denglu_kaishi('cemaxueyuan02','cema123456')


    def test_login_error(self):
        logging.info('=======test_login_error=========')
        l=denglu(self.driver)
        l.denglu_kaishi('666','222')

