#coding=utf-8
import unittest
from KeyWords_demo.web_keywords import WebUIKeys
from log.log import Logger
import os
from BeautifulReport import BeautifulReport


log=Logger().get_logger()


class UnitDemo(unittest.TestCase):
    # 失败截图方法（必须定义在class中）
    def save_img(self, img_name):
        # 保存路径
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        # root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
        img_path = root_dir + '/img'
        self.wk.copy_img('{}\{}.png'.format(img_path,img_name))

    @classmethod
    def setUpClass(cls):
        cls.wk = WebUIKeys('Chrome')

    @classmethod
    def tearDownClass(cls):
        pass
    # def setUp(self):
    #     print('正在开始测试')
    #
    # def tearDown(self):
    #     print('结束测试')
    def test_01(self):
        a={"txt":"http://www.baidu.com"}
        self.wk.url(**a)
    def test_03(self):
        b={"name":"id","value":"kw","txt":"许三多"}
        self.wk.input(**b)
    def test_02(self):
        t={"txt":10}
        self.wk.wait(**t)
    def test_05(self):
        d={"txt":5}
        self.wk.sleep(**d)
    def test_04(self):
        c={"name":"id","value":"su"}
        self.wk.click(**c)
    # 想要失败后的截图，需要装饰器
    @BeautifulReport.add_test_img('测试截图')
    def test_06(self):
        e={"name":"xpath","value":'//*[@id="rs"]/div/table/tbody/tr[1]/th[1]/a',"expect":"许三多"}
        result=self.wk.assert_text(**e)
        self.assertEqual(True,result)
    def test_07(self):
        f={"txt":2}
        self.wk.sleep(**f)
    def test_08(self):
        self.wk.quit()
    @unittest.skip
    def test_09(self):
        print('测试错误')


if __name__ == '__main__':
   unittest.main()