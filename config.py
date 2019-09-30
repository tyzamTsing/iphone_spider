#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/7/31 下午10:19
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: config
# @Software: PyCharm
import os
from datetime import datetime
from toolkit.config import BaseConfig, get_current_config

__author__ = 'blackmatrix'


class CommonConfig(BaseConfig):

    # 项目路径
    PROJ_PATH = os.path.abspath('')
    # ServerChan
    SEC_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    # Apple Store Url
    APPLE_STORES_URL = 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/stores.json'
    # iPhone库存
    IPHONE_MODELS_URL = 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability.json'
    # 部分 iPhone 型号
    MODELS = {
        'MWD92CH/A': 'iPhone 11 Pro 深空灰 64GB',
        'MWDD2CH/A': 'iPhone 11 Pro 暗夜绿 64GB',
        'MWDE2CH/A': 'iPhone 11 Pro 深空灰 256GB',
        'MWDH2CH/A': 'iPhone 11 Pro 暗夜绿 256GB',
        'MWEV2CH/A': 'iPhone 11 Pro Max 深空灰 256GB',
        'MWF42CH/A': 'iPhone 11 Pro Max 暗夜绿 256GB'
    }

    # 监控时间段
    WATCH_START = datetime.strptime('6:50:00', '%H:%M:%S').time()
    WATCH_END = datetime.strptime('22:59:59', '%H:%M:%S').time()
    # 监控型号
    BUY_MODELS = ['MWF42CH/A']
    BUY_CITY = '上海'
    BUY_STORES = ['R390']


commoncfg = CommonConfig()

configs = {
    'default': commoncfg
}

# 读取配置文件的名称，在具体的应用中，可以从环境变量、命令行参数等位置获取配置文件名称
config_name = 'default'

current_config = get_current_config(configs, config_name)
