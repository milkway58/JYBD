#-*- coding:utf-8 -*-
# Autor:wangtong

import unittest
from lib.readexceldata import read_excel
from lib.read_login import login
from lib.model import Test

"""
地区接口测试
"""

class Area(unittest.TestCase):
    """获取地址列表"""
    @classmethod
    def setUpClass(self):
        # login()
        pass
    @classmethod
    def tearDownClass(self):
        pass

    # @unittest.skip("test_01 ship")
    def test_01getAreaList(self):
        """获取地址列表"""
        Test.get_model(self, 'getAreaList', read_excel('system'))

    @unittest.skip("test_02 skip")
    def test_02getAreaList(self):
        """获取地区详情"""
        Test.post_model(self, 'getAreaList', read_excel('system'))

    @unittest.skip("test_03 skip")
    def test_03getAllArea(self):
        """获取全部地址"""
        # 无权限
        Test.post_model(self, 'getAllArea', read_excel('system'))

    @unittest.skip("test_04 skip")
    def test_04addArea(self):
        """添加地区"""
        Test.post_model(self, 'addArea', read_excel('system'))

    @unittest.skip("test_05 skip")
    def test_05editArea(self):
        """修改"""
        Test.post_model(self, 'delArea', read_excel('system'))

    @unittest.skip("test_06 skip")
    def test_06delArea(self):
        """删除一个地区"""
        Test.post_model(self, 'addArea', read_excel('system'))

if __name__ == '__main__':
    unittest.main(verbosity=2)



