# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 14:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : Log.py
# @Software: PyCharm

import logging
import logging.config
from config.VarConfig import *

logging.config.fileConfig(parentDirPath + '\config\Logger.conf')
logger = logging.getLogger('example01')

def debug(message):
    logger.debug(message)

def info(message):
    logger.info(message)

def warning(message):
    logger.warning(message)