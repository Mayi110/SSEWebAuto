# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 9:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : TestSSESearch.py
# @Software: PyCharm

from selenium import webdriver
from appModules.SSESearchAction import sseSearchAction
from util.Log import *

driver = None


def test_searchCompanyCodeEnterWebSearchPage():
    global driver
    try:
        logging.info('场景：通过公司代码查询，进入全文检索页面 测试开始。。。')
        sseSearchAction.LaunchBrowser('chrome','http://www.sse.com.cn')
        sseSearchAction.sseSearchEnterWebSWDPage('600015','华夏银行')
    except Exception as e:
        raise e

# def test_searchCompanyCodeEnterAnnouncementPage():
#     try:
#         driver = LaunchBrowser()
#         sseSearchAction.sseSearchEnterAnnouncementPage(driver,'600015','上市公司公告全文')
#     except Exception as e:
#         raise e
#     finally:
#         driver.quit()
