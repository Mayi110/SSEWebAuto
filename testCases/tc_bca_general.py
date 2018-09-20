# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 15:01
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bca_general.py
# @Software: PyCharm

from action.commonAction import *
from appModules.am_disclosure.am_announcement.am_general import generalAction
from util.Log import *
import unittest
from selenium import webdriver
from config.VarConfig import *
import ddt

url = testUrl+'/disclosure/announcement/general/'

@ddt.ddt
class generalCase(unittest.TestCase):
    '''一般公告测试用例集合'''

    @ddt.data(['chrome','富国中证','1','富国中证10年期国债交易型开放式'])
    @ddt.unpack
    def test_searchGeneralByAllCondition(self,browserName,testData01,testData02,expectData):
        '''通过全条件查询一般公告信息'''
        try:
            logging.info('场景：通过一般公告全条件查询，进入详情页面 测试开始。。。')
            launchBrowser(browserName,url)
            generalAction.searchGeneralByAllCondition(webdriver,testData01,testData02)
            assertPageElement(expectData)
        except Exception as e:
            raise e



if __name__ == '__main__':
    unittest.main()