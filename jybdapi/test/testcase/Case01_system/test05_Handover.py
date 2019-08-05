#-*- coding:utf-8 -*-
# Autor:wangtong

import unittest,requests
from lib.readexceldata import read_excel
from lib.read_login import login,getToken,wanHeader
from lib.model import Test
from lib import readexceldata
from config.config import read_log

"""
单据信息管理接口测试
"""
class Handover(unittest.TestCase):
    """单据信息管理"""
    @classmethod
    def setUpClass(self):
        login()
        # pass
    @classmethod
    def tearDownClass(self):
        pass

    # @unittest.skip("test_01 ship")
    def test_01getHandoverList(self):
        """交货方式列表"""

        data = readexceldata.get_test_data('getHandoverList', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        expire_result = int(data['expire_result'])
        params = {'token': getToken(), 'sign': '123456',}
        r = requests.get(url, params)
        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual(result, expire_result)
        hand_over_id = r.json()['data']['data'][0]['hand_over_id']
        return hand_over_id

    # @unittest.skip("test_02 skip")
    def test_02getHandoverInfo(self):
        """交货方式详情"""

        data = readexceldata.get_test_data('getHandoverInfo', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        expire_result = int(data['expire_result'])

        params = {'token': getToken(), 'sign': '123456', 'hand_over_id': '10005'}
        r = requests.get(url, params)

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual(result, expire_result)

    # @unittest.skip("test_03 skip")
    def test_03addHandover(self):
        """新增交货方式"""
        Test.post_model(self, 'addHandover', read_excel('system'))

    # @unittest.skip("test_04 skip")
    def test_04editHandover(self):
        """修改交货方式"""

        new_hand_over_id= Handover.test_01getHandoverList(self)
        data = readexceldata.get_test_data('editHandover', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        input_payload = eval(data['input_payload'])
        input_payload['hand_over_id']=new_hand_over_id

        expire_result = int(data['expire_result'])
        r = requests.post(url,data=input_payload,headers=wanHeader())
        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual( result, expire_result)

    # @unittest.skip("test_05 skip")
    def test_05delHandover(self):
        """删除交货方式"""

        new_hand_over_id= Handover.test_01getHandoverList(self)
        data = readexceldata.get_test_data('delHandover', read_excel('system'))
        read_log.case_log(data)
        url = data['url']
        input_payload = eval(data['input_payload'])
        input_payload['hand_over_id'] = new_hand_over_id

        expire_result = int(data['expire_result'])
        r = requests.post(url, data=input_payload, headers=wanHeader())

        # logging.info("响应内容:%s" % r.text)
        result = r.json()['code']
        self.assertEqual(result, expire_result)

if __name__ == '__main__':
    unittest.main(verbosity=2)



