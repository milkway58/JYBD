#-*- coding:utf-8 -*-
# Autor:wangtong

import unittest
import requests
from lib.readexceldata import read_excel
from lib.read_login import login
from lib.model import Test
from lib import readexceldata
from config.config import read_log
import logging,time
from lib.read_login import getToken,wanHeader

"""
客户期初接口测试
"""

class CustomerBalance(unittest.TestCase):
    """客户期初"""
    @classmethod
    def setUpClass(self):
        # pass
        login()
        # print('*****测试执行开始*****\n')
    @classmethod
    def tearDownClass(self):
        pass
        # print('*****测试执行完毕*****')

# ------------客户期初--------------
#     @unittest.skip("test_01 ship")
    def test_01downloadFileUrl(self):
        """获取客户期初应收余额下载模板地址"""
        Test.get_model(self,'customerdownloadFileUrl', read_excel('system'))

    # @unittest.skip("test_02 skip")
    def test_02addCustomerBeginningBalance(self):
        """新增客户期初应收余额"""
        Test.post_model(self,'addCustomerBeginningBalance', read_excel('system'))

    # @unittest.skip("test_03 ship")
    def test_03getCustomerBeginningBalanceList(self):
        """获取客户期初应收余额列表"""
        data = readexceldata.get_test_data('getCustomerBeginningBalanceList', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        expire_result = int(data['expire_result'])
        params = {'token': getToken(), 'sign': '123456',}
        r = requests.get(url, params)
        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual(result, expire_result)
        new_beginning_customer_balance_id = r.json()['data']['data'][0]['beginning_customer_balance_id']
        return new_beginning_customer_balance_id

    # @unittest.skip("test_04 ship")
    def test_04getCustomerBeginningBalanceInfo(self):
        """获取客户期初应收余额详情"""

        data = readexceldata.get_test_data('getCustomerBeginningBalanceInfo', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        expire_result = int(data['expire_result'])

        params = {'token': getToken(), 'sign': '123456', 'customer_balance_id': '10283'}
        r = requests.get(url, params)

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual(result, expire_result)

    # @unittest.skip("test_05 ship")
    # def test_05importCustomerBalance(self):
    #     """批量导入客户期初应收余额"""
    #     # 因post无法发送excel文件请求，暂时略过
    #     pass


    # @unittest.skip("test_06 skip")
    def test_06editCustomerBeginningBalance(self):
        """修改客户期初应收余额"""
        new_id= CustomerBalance.test_03getCustomerBeginningBalanceList(self)
        data = readexceldata.get_test_data('editCustomerBeginningBalance', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        input_payload = eval(data['input_payload'])
        input_payload['balance_id']=new_id

        expire_result = int(data['expire_result'])
        r = requests.post(url,data=input_payload,headers=wanHeader())
        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

    # @unittest.skip("test_07 skip")
    def test_07delCustomerBeginningBalance(self):
        """删除客户期初应收余额"""
        new_id= CustomerBalance.test_03getCustomerBeginningBalanceList(self)
        data = readexceldata.get_test_data('delCustomerBeginningBalance', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        input_payload = eval(data['input_payload'])
        input_payload['beginning_customer_balance_id'] = new_id

        expire_result = int(data['expire_result'])
        r = requests.post(url, data=input_payload, headers=wanHeader())

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual(result, expire_result)


    @unittest.skip("test_08 skip")
    def test_08auditorPass(self):
        """审核客户期初应收余额"""

        Test.post_model(self,'auditorPass', read_excel('system'))


if __name__ == '__main__':
    unittest.main(verbosity=2)



