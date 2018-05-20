# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 15:06
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_inquiries.py
# @Software: PyCharm

from selenium import webdriver
from appModules.am_disclosure.am_credibility.am_supervision.am_inquiries import inquiriesAction
from util.Log import *
import unittest


class inquiriesCase(unittest.TestCase):
    '''监管问询测试用例'''
    def test_searchInquiriesByAllCondition(self):
        '''通过全条件查询监管问询公司信息'''
        try:
            logging.info('场景：通过监管公司全条件查询，进入pdf页面 测试开始。。。')
            inquiriesAction.LaunchBrowser('chrome','http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/')
            inquiriesAction.searchMeasuresByAll(webdriver,'600086','定期报告事后审核意见函','2018-05-01','2018-05-17')
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()

