#-*- coding:utf-8 -*-
# Autor:wangtong
# Data: 2019-06-10
# request请求类型封装

from lib import readexceldata,case_log
import logging
import requests
from lib.read_login import getToken,wanHeader
import unittest
from lib.readexceldata import read_excel

# , 'customer_balance_id': '10266'
class Test(unittest.TestCase):
    def get_model(self,c1,c2):
        """get请求类型"""
        data = readexceldata.get_test_data(c1, c2)
        case_log.case_log(data)
        url = data['url']
        expire_result = int(data['expire_result'])

        # # input_payload = eval(data['input_payload'])
        # r = requests.post(url,data=input_payload,headers=wanHeader())
        params = {'token': getToken(), 'sign': '123456'}
        r = requests.get(url, params)

        logging.info("响应内容:%s" % r.text)
        result = int(r.json()['code'])
        self.assertEqual(result, expire_result)

    def post_model(self,c1,c2):
        """post 请求类型"""
        data = readexceldata.get_test_data(c1, c2)
        case_log.case_log(data)
        url = data['url']
        input_payload = eval(data['input_payload'])
        expire_result = int(data['expire_result'])
        r = requests.post(url,data=input_payload,headers=wanHeader())

        logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

# if __name__ == '__main__':
#     # unittest.main()
#     test = Test()
#     test.get_model('CostRecalculationAdd', read_excel('system'))
#     # Test.get_model(self, 'CostRecalculationAdd', read_excel('system'))




