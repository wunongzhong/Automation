import jsonpath
import json

from tools.log import logger
depend = {}
class operatorConvert:
    def convertBody(self, body):
        logger.info("找出存在可变变量区间块。。。。")
        # 找出变量区间块
        # strsplitvar = body.split('$')[1]
        try:
            listsplitvar = body.split('$')
            num = 0
            for strrequest in listsplitvar:
                logger.info("分割字符串。。。。")
                # 从$分割字符串，奇数的得到要取代的块
                if num % 2 == 1:
                    # 取代的块赋值给strchuck
                    strchuck = strrequest
                    # 找到全局变量名称
                    logger.info("找块中全局变量的名称。。。。")
                    stevar = strchuck[:strchuck.find('.')]
                    # 从depend获取变量值
                    logger.info("获取全局变量json值。。。。")
                    varvalue = depend[stevar]
                    varvalue = str(varvalue, encoding="utf-8")
                    # 得到变量后面的jsonpath
                    logger.info("获取块中jsonpath。。。。")
                    varjsonpath = strchuck[strchuck.find('.') + 1:]
                    varjsonresult = json.loads(varvalue)

                    # 从全局变量中获取到jsonpath里面的值
                    logger.info("由jsonpath从全局变量里面取值并替换变量块。。。。")
                    varchuck = jsonpath.jsonpath(varjsonresult, expr='$.' + varjsonpath)
                    listsplitvar[num] = str(varchuck[0])

                num = num + 1

            strsplitvar=''.join(listsplitvar)
        except Exception as e:
            logger.error("替换变量块出错，请查看问题！原因: s%", e)

        return strsplitvar
