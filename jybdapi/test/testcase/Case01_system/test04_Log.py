#-*- coding:utf-8 -*-
# Autor:wangtong

import unittest
from lib.readexceldata import read_excel
from lib.read_login import login
from lib.model import Test

"""
日志导出接口测试
"""

class Log(unittest.TestCase):
    """日志管理"""
    @classmethod
    def setUpClass(self):
        # login()
        pass

    @classmethod
    def tearDownClass(self):
        pass

    #     @unittest.skip("test_01 ship")
    def test_01exportLoginQuitLogUrl(self):
        """导出上级日志"""
        Test.get_model(self, 'exportLoginQuitLogUrl', read_excel('system'))

    # @unittest.skip("test_02 skip")
    def test_02getLoginQuitLogList(self):
        """获取上级日志列表"""
        Test.get_model(self,'getLoginQuitLogList', read_excel('system'))

    @unittest.skip("test_03 skip")
    def test_03delLoginQuitLog(self):
        """删除上机日志"""
        Test.post_model(self,'delLoginQuitLog', read_excel('system'))

    # @unittest.skip("test_04 skip")
    def test_04exportActionLogUrl(self):
        """导出业务日志"""
        Test.get_model(self,'exportActionLogUrl', read_excel('system'))

    # @unittest.skip("test_05 skip")
    def test_05getActionLogList(self):
        """获取上级日志列表"""
        Test.get_model(self,'getActionLogList', read_excel('system'))

    @unittest.skip("test_06 skip")
    def test_06delActionLog(self):
        """删除业务日志"""
        Test.post_model(self,'delActionLog', read_excel('system'))

if __name__ == '__main__':
    unittest.main(verbosity=2)



