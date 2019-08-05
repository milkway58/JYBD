#-*- coding:utf-8 -*-
# Autor:wangtong

import unittest,requests,logging
from lib.readexceldata import read_excel
from config.config import read_log
from lib.model import Test
from lib import readexceldata
from lib.read_login import getToken,wanHeader

"""
左侧菜单和商品基本信息接口测试
"""

class Menu_CompanyGoods(unittest.TestCase):
    """商品基本信息"""
    @classmethod
    def setUpClass(self):
        # login()
        pass
    @classmethod
    def tearDownClass(self):
        print('\n*****测试执行完毕*****')

    # @unittest.skip("test_01 ship")
    def test_01getLeftMenuList(self):
        """左侧菜单列表"""
        Test.get_model(self, 'getLeftMenuList', read_excel('system'))

    # @unittest.skip("test_02 ship")
    def test_02addUnit(self):
        """新增商品计量单位"""
        Test.post_model(self, 'addUnit', read_excel('system'))

    # @unittest.skip("test_03 ship")
    def test_03getUnitList(self):
        """获取商品计量单位"""
        Test.get_model(self, 'getUnitList', read_excel('system'))

        data = readexceldata.get_test_data('getUnitList', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        expire_result = int(data['expire_result'])

        params = {'token': getToken(), 'sign': '123456',}
        r = requests.get(url, params)

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual(result, expire_result)

        new_unit_id = r.json()['data']['data'][0]['unit_id']
        return new_unit_id

    # @unittest.skip("test_04 skip")
    def test_04editUnit(self):
        """修改商品计量单位"""
        new_unit_id= Menu_CompanyGoods.test_03getUnitList(self)
        data = readexceldata.get_test_data('editUnit', read_excel('system'))

        read_log.case_log(data)
        url = data['url']
        input_payload = eval(data['input_payload'])
        input_payload['unit_id']=new_unit_id

        expire_result = int(data['expire_result'])
        r = requests.post(url,data=input_payload,headers=wanHeader())

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

    # @unittest.skip("test_05 skip")
    def test_05delUnit(self):
        """删除商品计量单位"""
        new_unit_id= Menu_CompanyGoods.test_03getUnitList(self)
        data = readexceldata.get_test_data('delUnit', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        input_payload = eval(data['input_payload'])
        input_payload['unit_id']=new_unit_id

        expire_result = int(data['expire_result'])
        r = requests.post(url,data=input_payload,headers=wanHeader())

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

    # @unittest.skip("test_06 ship")
    def test_06addNameRule(self):
        """新增生成规格"""

        Test.post_model(self, 'addNameRule', read_excel('system'))

    # @unittest.skip("test_07 ship")
    def test_07getNameRuleList(self):
        """获取生成规格列表"""

        data = readexceldata.get_test_data('getNameRuleList', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        expire_result = int(data['expire_result'])

        params = {'token': getToken(), 'sign': '123456',}
        r = requests.get(url, params)

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual(result, expire_result)

        new_rule_id = r.json()['data']['data'][0]['rule_id']
        return new_rule_id

    # @unittest.skip("test_08 skip")
    def test_08getNameRuleInfo(self):
        """获取指定的名称生成规则信息"""
        new_rule_id= Menu_CompanyGoods.test_07getNameRuleList(self)
        data = readexceldata.get_test_data('getNameRuleList', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        expire_result = int(data['expire_result'])

        params = {'token': getToken(), 'sign': '123456','rule_id':new_rule_id}
        r = requests.get(url, params)

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual(result, expire_result)

    # @unittest.skip("test_09 skip")
    def test_09editNameRule(self):
        """编辑生成规格"""
        new_rule_id= Menu_CompanyGoods.test_07getNameRuleList(self)
        data = readexceldata.get_test_data('editNameRule', read_excel('system'))

        read_log.case_log(data)
        url = data['url']
        input_payload = eval(data['input_payload'])
        input_payload['rule_id']=new_rule_id

        expire_result = int(data['expire_result'])
        r = requests.post(url,data=input_payload,headers=wanHeader())

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

    # @unittest.skip("test_10skip")
    def test_10delNameRule(self):
        """删除生成规格"""
        new_rule_id= Menu_CompanyGoods.test_07getNameRuleList(self)
        data = readexceldata.get_test_data('delNameRule', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        input_payload = eval(data['input_payload'])
        input_payload['rule_id']=new_rule_id

        expire_result = int(data['expire_result'])
        r = requests.post(url,data=input_payload,headers=wanHeader())

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

if __name__ == '__main__':
    unittest.main(verbosity=2)



