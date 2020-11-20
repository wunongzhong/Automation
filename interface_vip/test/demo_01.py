#coding=utf-8
import hashlib
import time
from datetime import datetime
import requests

# 方法1     验签加密
def signmake():
    # appkey
    appkey = "598d0e89a703477aabe5406e321515b6"
    # 请求url
    url = "https://route.showapi.com/64-19?com=yuantong&nu=YT4620020577123&showapi_appid=298130&showapi_timestamp={{time}}&showapi_sign={{sign}}"
    # 生成数组把？后面的&分裂，排成一个list
    params = url.split("?")[1].split("&")
    #
    if len(params) > 0:
        str_parm = ""
        # 时间格式生成showapi_timestamp
        timereplace = datetime.now().strftime("%Y%m%d%H%M%S")
        for p in sorted(params):
            # 如果是showapi_sign  不参与签名
            if p.split("=")[0] == "showapi_sign":
                continue
            # 如果是showapi_timestamp  我就要重新赋值now给他
            if p.split("=")[0] == "showapi_timestamp":
                now = timereplace
                str_parm += p.split("=")[0] + now
            else:
                # 要参与签名的其他参数
                str_parm += p.split("=")[0] + p.split("=")[1]
        # 拼装一个密钥加在后面
        str_parm += appkey
        # 生成MD5sign
        sign = hashlib.md5(str_parm.encode()).hexdigest()
        # 替换两个参数
        url = url.replace("{{time}}", timereplace)
        url = url.replace("{{sign}}", sign)
        return url

# 方法2
def yanqianjiami():
    url = "https://route.showapi.com/64-19?com=yuantong&nu=YT4620020577123&phone=13566661111&showapi_appid=431684&showapi_timestamp={}&showapi_sign={}"
    param = url.split("?")[1]
    if param:
        time1 =time.strftime('%Y%m%d%H%M%S',time.localtime())
        param += "&showapi_timestamp=" + time1
        params = param.split("&")
        params.sort()
        keys=[]
        values=[]
        for i in range(len(params)):
            keys.append(params[i].split("=")[0])
            values.append(params[i].split("=")[1])
        str = []
        for i in range(len(keys)):
            if values[i] == "{}":
                continue
            str.append(keys[i] + values[i])
        sign = "".join(str)
        sign = sign + "598d0e89a703477aabe5406e321515b6"
        result = hashlib.md5(sign.encode("utf-8")).hexdigest()
        url = "https://route.showapi.com/64-19?com=yuantong&nu=YT4620020577123&phone=13566661111&showapi_appid=431684&showapi_timestamp={}&showapi_sign={}".format(time,result)
        return url
# res = requests.get(url)
# print(res.json())