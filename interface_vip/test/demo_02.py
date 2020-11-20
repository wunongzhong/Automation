#coding=utf-8
import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    vardict={}
    def test_1login(self):
        url = "http://localhost:5000/api/login"
        data = {"username": "admin", "password": "123456"}
        header = {"content-type": "application/json"}
        res = requests.post(url, headers=header, data=json.dumps(data))
        resjson = res.json()
        MyTestCase.vardict["login"]=resjson
        msg = jsonpath.jsonpath(MyTestCase.vardict["login"], "$.msg")[0]
        self.assertEqual("success", msg)

    def test_2userinfo(self):
        url = "http://localhost:5000/api/getuserinfo"
        #使用dict的变量取值
        headervalue=jsonpath.jsonpath(MyTestCase.vardict["login"],"$.token")[0]
        header = {"token": headervalue}
        res=requests.get(url,headers=header)
        resjson=res.json()
        MyTestCase.vardict["userinfo"] = resjson
        httpcode=jsonpath.jsonpath(MyTestCase.vardict["userinfo"], "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

    def test_3productinfo(self):
        url="http://localhost:5000/api/getproductinfo?productid=8888"
        res = requests.get(url)
        resjson=res.json()
        MyTestCase.vardict["productinfo"] = resjson
        httpcode = jsonpath.jsonpath(MyTestCase.vardict["productinfo"], "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

    def test_4addcart(self):
        url="http://localhost:5000/api/addcart"
        tokenout=jsonpath.jsonpath(MyTestCase.vardict["login"], "$.token")[0]
        userid=jsonpath.jsonpath(MyTestCase.vardict["userinfo"], "$.data[0].userid")[0]
        openid = jsonpath.jsonpath(MyTestCase.vardict["userinfo"], "$.data[0].openid")[0]
        productid = jsonpath.jsonpath(MyTestCase.vardict["productinfo"], "$.data[0].productid")[0]
        header={"token":tokenout,"content-type":"application/json"}
        data={"userid":userid,"openid":openid,"productid":productid}
        data=json.dumps(data)
        res=requests.post(url,headers=header,data=data)
        resjson=res.json()
        MyTestCase.vardict["addcart"] = resjson
        httpcode = jsonpath.jsonpath(MyTestCase.vardict["addcart"], "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

    def test_5createorder(self):
        url="http://localhost:5000/api/createorder"
        tokenout = jsonpath.jsonpath(MyTestCase.vardict["login"], "$.token")[0]
        userid = jsonpath.jsonpath(MyTestCase.vardict["userinfo"], "$.data[0].userid")[0]
        openid = jsonpath.jsonpath(MyTestCase.vardict["userinfo"], "$.data[0].openid")[0]
        productid = jsonpath.jsonpath(MyTestCase.vardict["productinfo"], "$.data[0].productid")[0]
        cartid = jsonpath.jsonpath(MyTestCase.vardict["addcart"], "$.data[0].cartid")[0]
        header = {"token": tokenout, "content-type": "application/json"}
        data={"userid":userid,"openid":openid,"productid":productid,"cartid":cartid}
        data=json.dumps(data)
        res=requests.post(url,headers=header,data=data)
        resjson=res.json()
        httpcode = jsonpath.jsonpath(resjson, "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

if __name__ == '__main__':
    unittest.main()
