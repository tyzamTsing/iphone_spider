#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 9:33 AM
# @Author  : Matrix
# @Site    : 
# @Software: PyCharm
import os
import logging
from time import sleep
from extensions import r
from datetime import datetime
from config import current_config
from toolkit.initlogs import log_init

__author__ = 'BlackMatrix'

# 初始化日志配置文件
log_init(file=os.path.abspath('logging.cfg'))

SEND_MSG_TIME = {}

APPLE_STORES = {}

STORES_STOCK = {}


def get_apple_stores(select_city=None):
    """
    获取所有的Apple Store信息，并按城市分类
    也可以获取单个城市的零售店信息
    :return:
    """
    if not APPLE_STORES:
        resp = r.get(current_config['APPLE_STORES_URL'])
        for store in resp.json()['stores']:
            if store['enabled'] is True:
                city = APPLE_STORES.setdefault(store['city'], {})
                city.update({store['storeNumber']: store['storeName']})

    return APPLE_STORES if select_city is None else APPLE_STORES.get(select_city)


def get_store_name(store_code):
    """
    根据Apple Store编号获取名称
    :param store_code:
    :return:
    """
    stores = get_apple_stores()
    for city, store in stores.items():
        for code, name in store.items():
            if code == store_code:
                return name


def get_model_name(part_num):
    """
    根据型号获取设备名称
    :param part_num:
    :return:
    """
    models = current_config.MODELS
    for model_part_num, model_name in models.items():
        if model_part_num == part_num:
            return model_name


def search_iphone():
    availability = r.get(current_config['IPHONE_MODELS_URL']).json()
    # 获取目标商店
    target_stores = current_config.BUY_STORES if current_config.BUY_STORES and len(current_config.BUY_STORES) > 0 \
        else get_apple_stores(current_config.BUY_CITY).keys()
    # 处理库存
    if availability['stores']:
        for store in target_stores:
            # 遍历目标型号
            for model_number in current_config.BUY_MODELS:
                # 获取型号名称和商品名称
                store_name = get_store_name(store)
                model_name = get_model_name(model_number)
                # 获取商品型号在店内的库存
                stock = availability['stores'][store][model_number]['availability']['unlocked']
                now = datetime.now()
                if STORES_STOCK.setdefault(model_name, {}).setdefault(store_name, {}).get('stock', False) is False and stock is True:
                    # 发送微信消息
                    msg = '发现库存，{0}，{1}, {2}'.format(store_name, model_name, now.strftime('%Y-%m-%d %H:%M:%S'))
                    r.get('http://sc.ftqq.com/{}.send?text={}已经有库存&desp={}'.format(
                        current_config.SEC_KEY, store_name, msg))
                    # 写入日志
                    logging.info(msg)
                # 库存从有到无时记录日志
                elif STORES_STOCK.setdefault(model_name, {}).setdefault(store_name, {}).get('stock') is True and stock is False:
                    msg = '库存售完，{0}，{1}，{2}'.format(store_name, model_name, now.strftime('%Y-%m-%d %H:%M:%S'))
                    # 写入日志
                    logging.info(msg)
                # 修改全局变量中的库存状态
                STORES_STOCK.setdefault(model_name, {}).setdefault(store_name, {}).update({'stock': stock, 'time': now})
        else:
            logging.info('库存没有变化')


def start():
    logging.info('开始监控设备库存信息')
    search_iphone()
    sleep(2)
    # 在有效的时间段内才查询库存
    while current_config.DEBUG or current_config['WATCH_START'] <= datetime.now().time() <= current_config['WATCH_END']:
        search_iphone()
        sleep(2)


if __name__ == '__main__':
    start()
