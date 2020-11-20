# -*- coding: utf-8 -*-
# @Time     : 2020/07/01
# @Author   : daniel
# @File     : common.py
# @Desc     : 框架数据驱动核心方法
# @Version  : V1.0.0

import requests
import json

from tools.log import logger
from tools.operator import getpost


class request_Common:

    def request(self, requestMethod, requestUrl, paramsType, requestData=None, headers=None):
        logger.info("执行统一请求方法开始。。。。。。。。。。。。。")
        # 判断requestMethod是否是post
        if requestMethod.lower() == "post":
            # paramsType是form表单提交
            if paramsType == "form":
                response = getpost().post(url=requestUrl, data=requestData, headers=headers
                                          )
                return response
            # json提交
            elif paramsType == 'json':
                requestData = eval(requestData)
                requestData = json.dumps(requestData)
                headers = eval(headers)
                #headers = json.dumps(headers)
                response = getpost().post(url=requestUrl, data=requestData, headers=headers
                                          )
                return response

        # 判断requestMethod是否是get
        elif requestMethod == "get":
            if paramsType == "url":

                request_url = "%s%s" % (requestUrl, "" if requestData is None else requestData)
                headers = eval(headers) if headers != '' else headers
                response = getpost().get(url=request_url, headers=headers)

                print(response)
                return response
            elif paramsType == "params":
                response = getpost().get(url=requestUrl, params=requestData, headers=headers)
                return response
