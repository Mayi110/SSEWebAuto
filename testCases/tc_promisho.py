# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 16:20
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_promisho.py
# @Software: PyCharm

from selenium import webdriver
from appModules.am_disclosure.am_credibility.am_supervision.am_promisho import promishoAction
from util.Log import *
import unittest

class promishoCase(unittest.TestCase):
    def test_searchPromishoByAllCondition(self):
        try:
            logging.info('场景：通过承诺履行全条件查询，进入详情页面 测试开始。。。')
            promishoAction.LaunchBrowser('chrome','http://www.sse.com.cn/disclosure/credibility/supervision/promisho/')
            promishoAction.searchPromishoByAll(webdriver,'603013','国家','1','1','2')
            promishoAction.assertPageElement('亚普股份')
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()

