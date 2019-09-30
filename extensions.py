#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/9/14 下午5:18
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : extensions.py
# @Software: PyCharm
import requests

__author__ = 'blackmatrix'

r = requests.Session()
r.headers.update(
    {'accept': 'application/json',
     'accept-encoding': 'gzip, deflate',
     'accept-language': 'en-US,en;q=0.8',
     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
     })

if __name__ == '__main__':
    pass
