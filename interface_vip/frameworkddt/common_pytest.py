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
import allure
import pytest
from tools.log import logger
from tools.operatorexcel import excelData
from requestcommon.request_common import request_Common
from tools.convertoperator import operatorConvert, depend

@allure.feature("登录测试")
class Test_Case:
    @allure.issue("http://www.jira.com")
    @allure.testcase("http://www.testlink.com")
    @allure.severity("critical")
    @pytest.mark.parametrize("case", excelData().get_excel_data())
    def test_commonapi(self,case):
        api=case[0]
        url=case[1]
        body=case[2]
        header=case[3]
        method=case[4]
        method_type=case[5]
        expect=case[6]
        jsonpaths=case[7]
        dependency=case[8]

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
        assert str(expect) == str(result[0])
