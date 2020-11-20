import requests

from tools.log import logger


class getpost:

    # requests的post请求
    def post(self, url, data=None, headers=None, **kargs):
        logger.info("执行post请求开始。。。。。。。。。。。。。")
        try:

            response = requests.post(url=url, data=data, headers=headers)
        except Exception as e:
            logger.error("执行post请求出错，请查看问题！原因: s%", e)
        return response

    # requests的get请求
    def get(self, url, params=None, headers=None, **kargs):
        logger.info("执行get请求开始。。。。。。。。。。。。")
        try:

            response = requests.get(url=url, params=params,headers=headers)
        except Exception as e:
            logger.error("执行get请求出错，请查看问题！原因: s%", e)
        return response