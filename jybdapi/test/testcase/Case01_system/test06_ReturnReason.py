#-*- coding:utf-8 -*-
# Autor:wangtong

import unittest
from lib.readexceldata import read_excel
from lib.read_login import login
from lib.model import Test

"""
销售退货原因管理接口测试
"""

class ReturnReason(unittest.TestCase):
    """销售退货原因管理"""
    @classmethod
    def setUpClass(self):
        # login()
        pass
    @classmethod
    def tearDownClass(self):
        pass

    # @unittest.skip("test_01 ship")
    def test_01getReasonList(self):
        """销售退货原因列表"""
        Test.get_model(self, 'getReasonList', read_excel('system'))

    @unittest.skip("test_02 skip")
    def test_02addReason(self):
        """新增销新增售退货原因"""
        Test.post_model(self, 'addReason', read_excel('system'))

    @unittest.skip("test_03 skip")
    def test_03editReason(self):
        """编辑增售退货原因"""
        Test.post_model(self, 'editReason', read_excel('system'))

    @unittest.skip("test_04 skip")
    def test_04delReason(self):
        """删除销新增售退货原因"""
        Test.post_model(self, 'delReason', read_excel('system'))

if __name__ == '__main__':
    unittest.main(verbosity=2)



