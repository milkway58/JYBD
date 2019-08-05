#-*- coding:utf-8 -*-
# Autor:wangtong

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

        login()
        # print('*****测试执行开始*****\n')
    @classmethod
    def tearDownClass(self):
        pass
        # print('\n*****测试执行完毕*****')

# ------------厂家期初--------------
    @unittest.skip("test_01 ship")
    def test_01downloadFileUrl(self):
        """获取厂家期初应收余额下载模板地址"""
        Test.get_model(self, 'supplierdownloadFileUrl', read_excel('system'))

    @unittest.skip("test_02 skip")
    def test_02addSupplierBeginningBalance(self):
        """新增厂家期初应收余额"""
        Test.post_model(self,'addSupplierBeginningBalance', read_excel('system'))

    # @unittest.skip("test_03 ship")
    def test_03getSupplierBeginningBalanceList(self):
        """获取厂家期初应收余额列表"""
        Test.get_model(self,'getSupplierBeginningBalanceList', read_excel('system'))

    # @unittest.skip("test_04 ship")
    def test_04getSupplierBeginningBalanceInfo(self):
        """获取厂家期初应收余额详情"""
        Test.get_model(self,'getSupplierBeginningBalanceInfo', read_excel('system'))

    # @unittest.skip("test_05 ship")
    # def test_05importSupplierBalance(self):
    #     """批量导入厂家期初应收余额"""
    #     # 因post无法发送excel文件请求，暂时略过
    #     pass

# #### 暂未实现 ####

    @unittest.skip("test_06 skip")
    def test_06editSupplierBeginningBalance(self):
        """修改厂家期初应收余额"""

        Test.post_model(self,'editSupplierBeginningBalance',read_excel('system'))

    @unittest.skip("test_07 skip")
    def test_07delSupplierBeginningBalance(self):
        """删除厂家期初应收余额"""

        Test.post_model(self,'delSupplierBeginningBalance',read_excel('system'))

    @unittest.skip("test_08 skip")
    def test_08auditorPass(self):
        """审核厂家期初应收余额"""

        Test.post_model(self,'auditorPass', read_excel('system'))


if __name__ == '__main__':
    unittest.main(verbosity=2)



