#-*- coding:utf-8 -*-
# Autor:wangtong
# Data: 2019-06-10

import unittest
from lib.readexceldata import read_excel
from lib.read_login import login
from lib.model import Test

"""
库存核算接口测试
"""

class CostRecalculation(unittest.TestCase):
    """库存核算"""
    @classmethod
    def setUpClass(self):

        login()
        print('*****测试执行开始*****\n')
    @classmethod
    def tearDownClass(self):
        pass
        # print('*****测试执行完毕*****')




    def test_02getCostRecalculationList(self):
        """成本重算列表"""

        Test.get_model(self,'getCostRecalculationList',read_excel('system'))


if __name__ == '__main__':
    unittest.main(verbosity=2)