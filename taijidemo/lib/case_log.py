#-*- coding:utf-8 -*-
# Autor:wangtong
# Data: 2019-06-10


from config.config import logger
"""
log文件配置
"""
def case_log(data):
    url = data['url']
    feature = data['feature']
    test_desc = data['test_desc']
    input_payload = data['input_payload']
    # input_headers = data['input_headers']
    expire_result = data['expire_result']

    logger.info("%s 测试开始" % feature)
    logger.info("%s 开始" % test_desc)
    logger.info("url: %s" % url)
    logger.info("请求头: %s" % input_payload)
    # logger.info("请求体: %s" % input_headers)
    logger.info("期望结果:%s" % expire_result)





