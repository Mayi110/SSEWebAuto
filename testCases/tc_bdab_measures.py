# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 11:07
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bdab_measures.py
# @Software: PyCharm

from selenium import webdriver
from appModules.am_disclosure.am_credibility.am_supervision.am_measures import measuresAction
from util.Log import *
import unittest


class measuresCase(unittest.TestCase):
    '''监管措施测试用例'''
    def test_searchMeasuresByAllCondition(self):
        '''通过全条件查询监管公司信息'''
        try:
            logging.info('场景：通过监管公司全条件查询，进入pdf页面 测试开始。。。')
            measuresAction.LaunchBrowser('chrome','http://www.sse.com.cn/disclosure/credibility/supervision/measures/')
            measuresAction.searchMeasuresByAll(webdriver,'600086','董秘','监管关注','2018-05-01','2018-05-17')
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()


