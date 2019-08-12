#-*- coding:utf-8 -*-
# Autor:wangtong
# Data: 2019-06-10

import unittest
from lib.readexceldata import read_excel
from lib.read_login import login
from lib.model import Test

"""
客户期初接口测试
"""

class CustomerBalance(unittest.TestCase):
    """客户期初"""
    @classmethod
    def setUpClass(self):
        pass
        # login()
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


    # @unittest.skip("test_02 ship")
    def test_02getCustomerBeginningBalanceList(self):
        """获取客户期初应收余额列表"""

        Test.get_model(self, 'getCustomerBeginningBalanceList', read_excel('system'))





if __name__ == '__main__':
    unittest.main(verbosity=2)



