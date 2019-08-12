#-*- coding:utf-8 -*-
# Autor:wangtong
# Data: 2019-06-10

import unittest
from lib.readexceldata import read_excel
from lib.read_login import login
from lib.model import Test

"""
厂家期初接口测试
"""

class SupplierBalance(unittest.TestCase):
    """厂家期初"""
    @classmethod
    def setUpClass(self):
        pass
        # login()
        # print('*****测试执行开始*****\n')



# ------------厂家期初--------------
#     @unittest.skip("test_01 ship")
    def test_01downloadFileUrl(self):
        """获取厂家期初应收余额下载模板地址"""

        Test.get_model(self, 'supplierdownloadFileUrl', read_excel('system'))

    # @unittest.skip("test_02 ship")
    def test_02getSupplierBeginningBalanceList(self):
        """获取厂家期初应收余额列表"""

        Test.get_model(self,'getSupplierBeginningBalanceList', read_excel('system'))

    # @unittest.skip("test_03 ship")
    def test_03getSupplierBeginningBalanceInfo(self):
        """获取厂家期初应收余额详情,故意错误"""

        Test.get_model(self,'getSupplierBeginningBalanceInfo', read_excel('system'))



    # @unittest.skip("test_05 skip")
    def test_04addSupplierBeginningBalance(self):
        """新增厂家期初应收余额"""

        Test.post_model(self,'addSupplierBeginningBalance', read_excel('system'))
# ####已测试完####3



    # @unittest.skip("test_07 skip")
    def test_05delSupplierBeginningBalance(self):
        """删除客户期初应收余额"""

        import requests
        from lib.read_login import getToken

        url = 'http://glterp.taijierp.cn/system/SupplierBalance/getSupplierBeginningBalanceList'
        params = {'token': getToken(), 'sign': '123456'}
        r = requests.get(url, params)
        print(r.json()['data']['data'][0]['beginning_supplier_balance_id'])
        ee = str(r.json()['data']['data'][0]['beginning_supplier_balance_id'])
        print(ee,type(ee))
        # print(r.text)
        from lib import readexceldata, case_log
        import logging
        import requests
        from lib.read_login import wanHeader

        data = readexceldata.get_test_data('delSupplierBeginningBalance',read_excel('system'))
        case_log.case_log(data)
        url = data['url']
        # input_payload = eval(data['input_payload'])
        expire_result = int(data['expire_result'])

        payload = eval(data['input_payload'])
        print(payload,type(payload))
        payload['beginning_supplier_balance_id'] = str(ee)
        input_payload = payload

        print(input_payload)
        r = requests.post(url,data=input_payload,headers=wanHeader())

        logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

        # Test.post_model(self,'delCustomerBeginningBalance',read_excel('system'))

    # @unittest.skip("test_08 skip")
    # def test_08auditorPass(self):
    #     """审核客户期初应收余额"""
    #
    #     Test.post_model(self,'auditorPass', read_excel('system'))


if __name__ == '__main__':
    unittest.main(verbosity=2)



