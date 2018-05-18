# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 9:26
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_detail.py
# @Software: PyCharm

import unittest
from appModules.am_market.am_othersdata.am_margin.am_detail import detailAction
from action.commonAction import *


class detailCase(unittest.TestCase):
    def test_searchSumByAllCondition(self):
        try:
            logging.info('场景：通过全部条件查询融资融券明细信息测试开始。。。')
            launchBrowser('chrome','http://www.sse.com.cn/market/othersdata/margin/detail/')
            detailAction.searchDetailByAllCondition(webdriver,'510500','2018-05-17')
            assertPageElement('595,158,136,870')
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()