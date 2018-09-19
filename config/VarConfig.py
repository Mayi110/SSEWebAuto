# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:17
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : VarConfig.py
# @Software: PyCharm

import os

# 文件路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 页面元素定位路径
pageElementLocatorPath = parentDirPath+'\\config\\PageElementLocator.ini'

# 浏览器驱动路径
ieDriverFilePath = 'c:\IEDriverServer'
fireFoxDriverFilePath = 'c:\FireFoxDriverServer'

# 截图存放路径
screenPictureDir = parentDirPath + '\\exceptionPictures\\'

# 设置不同环境下的url变量
# 测试环境
#testUrl = 'http://www108.sse.com.cn'

# 预发布环境
#testUrl = 'http://test.sse.com.cn'

# 生产环境
testUrl = 'http://www.sse.com.cn'
