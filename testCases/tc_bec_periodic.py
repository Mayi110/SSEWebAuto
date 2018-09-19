# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 14:40
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bec_periodic.py
# @Software: PyCharm

from appModules.am_disclosure.am_listedinfo.am_periodic import periodicAction
from util.Log import *
import unittest
from action.commonAction import *
from selenium import webdriver
from time import sleep


class periodicCase(unittest.TestCase):
    '''定期报告预约情况测试用例集合'''

    def test_searchPeriodicByAllConditionAndEnterRegularPage(self):
        '''通过全部查询条件查询定期报告预约情况后进入定期公告页面'''
        try:
            logging.info('场景：定期报告预约情况页面通过全部条件查询公告进入定期公告页面测试开始。。。')
            launchBrowser('chrome','http://www.sse.com.cn/disclosure/listedinfo/periodic/')
            sleep(5)
            periodicAction.searchPeriodicByAllConditionAndEnterRegularPage(webdriver,'600010')
            assertPageElement('定期报告')
        except Exception as e:
            raise e

    def test_searchPeriodicByAllConditionAndEnterCompanyInfoPage(self):
        '''通过全部查询条件查询定期报告预约情况后进入公司个股页面'''
        try:
            logging.info('场景：定期报告预约情况页面通过全部条件查询公告进入公司个股页面测试开始。。。')
            launchBrowser('chrome','http://www.sse.com.cn/disclosure/listedinfo/periodic/')
            sleep(5)
            periodicAction.searchPeriodicByAllConditionAndEnterCompanyInfoPage(webdriver,'600010')
            assertPageElement('内蒙古包钢钢联股份有限公司600010')
        except Exception as e:
            raise e
if __name__ == '__main__':
    unittest.main()