# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:17
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : VarConfig.py
# @Software: PyCharm

import os

parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pageElementLocatorPath = parentDirPath+'\\config\\PageElementLocator.ini'

ieDriverFilePath = 'c:\IEDriverServer'
fireFoxDriverFilePath = 'c:\FireFoxDriverServer'

screenPictureDir = parentDirPath + '\\exceptionPictures\\'
