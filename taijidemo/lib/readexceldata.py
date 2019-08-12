#-*- coding:utf-8 -*-
# Autor:wangtong
# Data: 2019-06-10

import xlrd
import os
from config.config import datapath

"""
读取excel表格封装方法
"""

def excel_to_list(file, tag):
    data_list = []
    book = xlrd.open_workbook(file)
    tag = book.sheet_by_name(tag)
    row_num = tag.nrows
    header = tag.row_values(0)
    for i in range(1, row_num):
        row_data = tag.row_values(i)
        d = dict(zip(header, row_data))
        data_list.append(d)
    return data_list


def get_test_data(test_name, test_list):
    for test_dict in test_list:
        if test_name == test_dict['test_name']:
            return test_dict

def read_excel(sheet_name):
    f = os.path.join(datapath, '接口测试用例.xls')
    data_list = excel_to_list(f, sheet_name)
    return data_list
    # print(data_list)

# 测试使用
# if __name__ == '__main__':
# read_excel('system')
#
#     file = os.path.join(datapath, '接口测试用例.xls')
#     tag = 'CostRecalculation'
#     test_list = excel_to_list(file, tag)
#     r=get_test_data('CostRecalculationAdd',test_list )
#     print(type(r),r)