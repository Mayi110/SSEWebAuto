# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 10:39
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bee_summaries.py
# @Software: PyCharm

from appModules.am_disclosure.am_listedinfo.am_summaries import summariesAction
from util.Log import *
import unittest
from action.commonAction import *
from selenium import webdriver
from time import sleep


class summariesCase(unittest.TestCase):
    '''公告摘要测试用例集合'''

    def test_searchPeriodicByAllConditionAndEnterRegularPage(self):
        '''通过全部查询条件查询公告摘要数据'''
        try:
            logging.info('场景：公告摘要页面通过全部条件查询公告测试开始。。。')
            launchBrowser('chrome','http://www.sse.com.cn/disclosure/listedinfo/summaries/')
            sleep(5)
            summariesAction.searchSummariesByAllCondition(webdriver,'603989','2018-05-01','2018-05-25')
            sleep(5)
            assertPageElement('(603989)“艾华集团”2018年第一季度主要财务指标')
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()