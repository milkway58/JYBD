# -*- coding: utf-8 -*-
# Autor:wangtong
# Data: 2019-06-10

import sys
import unittest
from config.config import reportpath,basedir
import time
from lib import send_email
from lib import HTMLTestRunner_PY3,HTMLTestRunner_PY4,HTMLTestRunner_cn

# cmd命令下添加环境变量
# sys.path.append('C:\\Users\\PC\\Desktop\\apiteststudy')

# 用例批量测试
suite = unittest.defaultTestLoader.discover(basedir + '/test/testcase')

curr_time = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
report_file= reportpath + '\\TestReport.html'

outfile = open(report_file, "wb")
runner = HTMLTestRunner_PY3.HTMLTestRunner(
    stream=outfile,
    title='Interface Test Report',
    description=u'接口测试报告.'
    )
runner.run(suite)
# send_email.send_email(report_file)
outfile.close()
