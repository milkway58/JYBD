import os
import logging
"""
config 目录配置
# Autor:wangtong
# Data: 2019-06-10
"""

#  项目目录

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置目录
configpath = os.path.join(basedir,'config')

# 数据目录
datapath = os.path.join(basedir,'data')

# 报告目录
reportpath = os.path.join(basedir, 'report')

# token 文件路径
tokenpath = os.path.join(configpath,'token.md')

#  日志配置
logdir = os.path.join(basedir, 'log')
logpath =os.path.join(logdir, 'log.txt')

# 邮件配置

# smtp_server = 'smtp.qq.com'
# port = '465'
# sender = '1044649245@qq.com'
# psw = 'xxx'
# receiver = '1044649245'

# log配置
logger = logging.getLogger('Interface_test')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(logpath, encoding='utf-8')

datafmt = "%Y-%m-%d %H:%M:%S"

fm = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt=datafmt)
fh.setFormatter(fm)
logger.addHandler(fh)
logging.getLogger("requests").setLevel(logging.WARNING)
# if __name__ == "__main__":
    # logger.info('this is test')
    #print(basedir)
    # print(configpath)
    # print(tokenpath)
