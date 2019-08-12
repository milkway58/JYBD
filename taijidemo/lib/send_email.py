#-*- coding:utf-8 -*-
# Autor:wangtong
# Data: 2019-06-10

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 密码:zpypjiegbayzbdje

# 发送邮件，发送最新测试报告html
def send_email(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 调试使用
    #    print u'打印'
    #    print mail_body
    # 关闭文件
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户名/密码
    user = '77996106@qq.com'
    password = 'xxx'
    # 发送邮箱
    sender = '77996106@qq.com'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['77996106@qq.com', '77996106@qq.com','77996106@qq.com']
    # 发送邮件主题
    subject = 'ERP接口自动化测试报告'

    msg = MIMEMultipart('mixed')

    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    msg['From'] = '77996106@qq.com'
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    print('=====AutoTest Start======')

    from config.config import reportpath
    new_report= os.path.join(reportpath,'TestReport.html')
    send_email(new_report)
    print('=====AutoTest Over======')
