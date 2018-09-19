# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 9:25
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_cjaa_sum.py
# @Software: PyCharm

from appModules.am_market.am_othersdata.am_margin.am_sum import sumAction
from util.Log import *
from action.commonAction import *
import unittest

class sumCase(unittest.TestCase):
    '''融资融券汇总测试用例'''

    def test_searchSumByAllCondition(self):
        '''通过全条件查询融资融券汇总信息'''
        try:
            logging.info('场景：通过全部条件查询融资融券汇总信息测试开始。。。')
            launchBrowser('chrome','http://www.sse.com.cn/market/othersdata/margin/sum/')
            sumAction.searchSumByAllCondition(webdriver,'510500','2018-05-16','2018-05-17')
            assertPageElement('20180517')
        except Exception as e:
            raise e