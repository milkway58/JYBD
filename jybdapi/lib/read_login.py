#-*- coding:utf-8 -*-
# Autor:wangtong
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
    r = requests.post(
        url='http://101.200.44.229/system/user/login',
        data={"sign": "123456", "username": "jiziting", "password": "123456", "client_type": 1},
        headers=getHeaders(), timeout=5)
    # print(r.text)
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