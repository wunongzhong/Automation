import jsonpath
import json

depend = {}


class operatorBody:
    def convertBody(self, body):
        # 找出变量区间块
        strsplitvar = body.split('$')[1]

        # 获取变量名称
        bodysplit = body[body.find('$') + 1:]

        strsplit = bodysplit[:bodysplit.find('.')]

        # 得到对应变量的接口返回值

        jsonresult = depend[strsplit]
        jsonresult = str(jsonresult, encoding="utf-8")

        # 得到变量后面的jsonpath
        strsplitsjsonpath = strsplitvar[strsplitvar.find('.') + 1:]
        jsonresult=json.loads(jsonresult)

        #从全局变量中获取到jsonpath里面的值
        result = jsonpath.jsonpath(jsonresult, expr='$.'+strsplitsjsonpath)

        #替换掉传入变量的值
        body = body.replace('$' + strsplitvar + '$', result[0])

        return body