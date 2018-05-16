# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 9:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : TestSSESearch.py
# @Software: PyCharm

from selenium import webdriver
from appModules.SSESearchAction import sseSearchAction
from util.Log import *


def test_searchCompanyCodeEnterWebSearchPage():
    try:
        logging.info('场景：通过公司代码查询，进入全文检索页面 测试开始。。。')
        sseSearchAction.LaunchBrowser(browserName='chrome',url='http://www.sse.com.cn')
        sseSearchAction.sseSearchEnterWebSWDPage(driver=webdriver,companyCode='600015')
        sseSearchAction.assertPageElement(assertString='华夏银行')
    except Exception as e:
        raise e

def test_searchCompanyCodeEnterAnnouncementPage():
    try:
        logging.info('场景：通过公司代码查询，进入全站检索页面 测试开始。。。')
        sseSearchAction.LaunchBrowser(browserName='chrome',url='http://www.sse.com.cn')
        sseSearchAction.sseSearchEnterAnnouncementPage(driver=webdriver,companyCode='白云机场')
        sseSearchAction.assertPageElement(assertString='广州白云国际机场股份有限公司')
    except Exception as e:
        raise e
