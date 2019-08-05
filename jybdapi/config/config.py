import logging, time
import os

"""
config 目录配置
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
# sender = '77996106@qq.com'
# psw = 'xxx'
# receiver = '77996106'

# log配置


# 存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)

class Log():
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

logg=Log()
class read_log():
    def case_log(data):
        url = data['url']
        feature = data['feature']
        test_desc = data['test_desc']
        input_payload = data['input_payload']
        # input_headers = data['input_headers']
        expire_result = data['expire_result']

        logg.info("%s 测试开始" % feature)
        logg.info("%s 开始" % test_desc)
        logg.info("url: %s" % url)
        logg.info("请求头: %s" % input_payload)
        # logger.info("请求体: %s" % input_headers)
        logg.info("期望结果:%s" % expire_result)

if __name__ == "__main__":
   log = Log()
   log.info("---测试开始----")
   log.info("操作步骤1,2,3")
   log.warning("----测试结束----")
