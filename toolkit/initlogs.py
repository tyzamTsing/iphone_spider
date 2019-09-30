# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2017/1/4 10:30
# Author: Matrix
# Site:
# File: log.py
# Software: PyCharm

import os
import logging
import traceback
import logging.config
from config import current_config
from datetime import datetime, timedelta

if not os.path.exists("logs"):
    os.mkdir("logs")


def log_init(file):
    try:
        logging.config.fileConfig(file, disable_existing_loggers=False)
    except Exception as ex:
        if not current_config.TESTING:
            pass
        else:
            f = open('logs/traceback.txt', 'a')
            traceback.print_exc()
            traceback.print_exc(file=f)
            f.flush()
            f.close()

#
# def beijing(sec, what):
#     beijing_time = datetime.now() + timedelta(hours=8)
#     return beijing_time.timetuple()
#
#
# logging.Formatter.converter = beijing
