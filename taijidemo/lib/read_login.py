#-*- coding:utf-8 -*-
# Autor:wangtong
# Data: 2019-06-10
# token封装
import requests
from config.config import tokenpath

"""
读取登录token
"""

def getHeaders():
    '''获取headers'''
    return {'Content-Type': 'application/x-www-form-urlencoded'}

def login():
    '''把token写入到文件中'''
    url = 'http://glterp.taijierp.cn/v2/user/Login/login'
    payload={"sign": "123456", "username": "xjy", "_userp":"Nzc5OTYxMDZ3dDIwMTktMDgtMTI=","client_type":"1"}
    r = requests.post(url=url, data=payload,headers=getHeaders())
    print(r.text)

    with open(token_dir(), 'w') as f:
        f.write(r.json()['data']['token'])

def token_dir():
    '''获取token.md的目录'''
    return tokenpath

def getToken():
    '''读取存储在文件中的token'''

    with open(token_dir(),'r') as f:
        return f.read()

# login()
# print(getToken())

def wanHeader():

    t=getHeaders()
    t['token']=getToken()
    return t
if __name__ == '__main__':
    login()