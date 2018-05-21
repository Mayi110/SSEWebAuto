# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 9:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_search.py
# @Software: PyCharm

from appModules.am_search.am_search import sseSearchAction
from action.commonAction import *
from time import sleep
import unittest
from selenium import webdriver
from action.commonAction import MyCommon


class searchCase(unittest.TestCase):
    '''全站检索测试用例'''

    # def test_enterWebSearchPageByCompanyCode(self):
    #     '''通过公司代码查询，进入全文检索页面'''
    #     try:
    #         logging.info('场景：通过公司代码查询，进入全文检索页面 测试开始。。。')
    #         launchBrowser('chrome','http://www.sse.com.cn')
    #         sseSearchAction.sseSearchEnterWebSWDPage(webdriver,'600015')
    #         assertPageElement('华夏银行')
    #     except Exception as e:
    #         raise e

    def test_enterAnnouncementPageByCompanyCode(self):
        '''通过公司代码查询，进入最新公告页面'''
        try:
            # logging.info('场景：通过公司代码查询，进入最新公告页面 测试开始。。。')
            MyCommon.launchBrowser(webdriver,'chrome','http://www.sse.com.cn')
            # driver = webdriver.Chrome()
            # driver.maximize_window()
            # driver.get('http://www.sse.com.cn')
            # sseSearchAction.sseSearchEnterAnnouncementPage(webdriver,'白云机场')
            # assertPageElement('广州白云国际机场股份有限公司')
            sleep(5)
            sseSearchAction.sseSearchEnterAnnouncementPage(webdriver,'浦发')
            # assert '张江高科' in driver.page_source
            MyCommon.assertPageElement(webdriver,'张江高科')
        except Exception as e:
            raise e


if __name__ == '__main__':
    # test_enterAnnouncementPageByCompanyCode()
    unittest.TestCase()