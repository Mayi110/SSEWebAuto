# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 9:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_h_search.py
# @Software: PyCharm

from appModules.am_search.am_search import sseSearchAction
from util.Log import *
from action.commonAction import *
import unittest
from time import sleep

class searchCase(unittest.TestCase):
    def test_enterWebSearchPageByCompanyCode(self):
        '''
        通过公司代码查询，进入全文检索页面
        '''
        try:
            logging.info('场景：通过公司代码查询，进入全文检索页面 测试开始。。。')
            launchBrowser('chrome','http://www.sse.com.cn')
            sleep(3)
            sseSearchAction.sseSearchEnterWebSWDPage(webdriver,'600015')
            assertPageElement('华夏银行')
        except Exception as e:
            raise e

    def test_enterAnnouncementPageByCompanyCode(self):
        '''
        通过公司代码查询，进入最新公告页面
        '''
        try:
            logging.info('场景：通过公司代码查询，进入最新公告页面 测试开始。。。')
            launchBrowser('chrome','http://www.sse.com.cn')
            sleep(3)
            sseSearchAction.sseSearchEnterAnnouncementPage(webdriver,'白云机场')
            assertPageElement('广州白云国际机场股份有限公司')
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()