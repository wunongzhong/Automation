# -*- coding: utf-8 -*-
# @Time     : 2020/07/01
# @Author   : daniel
# @File     : common.py
# @Desc     : 框架数据驱动核心方法
# @Version  : V1.0.0


import unittest
from datetime import time
import json
import jsonpath
from ddt import ddt, data, unpack

from tools.log import logger
from tools.operatorexcel import excelData
from requestcommon.request_common import request_Common
from tools.convertoperator import operatorConvert, depend


@ddt
class MyTestCase(unittest.TestCase):
    logger.info("执行测试用例开始。。。。")
    contents = []
    if len(contents) <= 0:
        logger.info("读取excel用例数据。。。。")
        casedata = excelData().getExcel()
        logger.info("循环读取excel中每行数据开始。。。。")
        for case in casedata:
            name = case
            listcase = casedata[name]
            for list in listcase:
                contents.append(list)
        logger.info("excel用例数据读取完成。。。。")

    @data(*contents)
    @unpack
    def test_get_commonapi(self, api, url, body, header, method, method_type, expect, jsonpaths, dependency):
        logger.info("用例数据拆包开始。。。。")
        common = request_Common()
        logger.info("替换body中的空格换行特殊字符开始。。。。")
        body = body.replace('\r', '').replace('\n', '').replace('\t', '') if body is not None else ""

        logger.info("转换存在可变变量开始。。。。")
        # 假如body中存在变量获取符号，调用convertBody重新对变量进行转化
        body = operatorConvert().convertBody(body) if body.find('$') >= 0 else body
        header = operatorConvert().convertBody(header) if (header is not None and header.find('$') >= 0) else header
        header = "" if header is None else header
        res = common.request(method, url, method_type, body, header)

        # 判断dependency是否有值需要存储

        if len(res.content) > 0 and dependency.find('/') < 0:
            depend[dependency] = res.content

        # 获取请求返回值
        resjson = json.loads(res.content)

        # 获得预期jsonpath路径下的值
        result = jsonpath.jsonpath(resjson, expr=jsonpaths)

        # code = res.status_code
        # print(code)
        # 断言预期值和实际返回值对比
        self.assertEqual(str(expect), str(result[0]))
