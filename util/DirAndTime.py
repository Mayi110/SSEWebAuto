# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 13:42
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : DirAndTime.py
# @Software: PyCharm

import time,os
from datetime import datetime
from config.VarConfig import screenPictureDir


# 获取当前的日期
def getCurrentDate():
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year) + '-' + str(timeTup.tm_mon) + '-' + str(timeTup.tm_mday)
    return currentDate


# 获取当前的时间
def getCurrentTime():
    timeStr = datetime.now()
    nowTime = timeStr.strftime('%H-%M-%S-%f')
    return nowTime


# 创建截图存放的目录
def createCurrentDateDir():
    dirName = os.path.join(screenPictureDir, getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName

