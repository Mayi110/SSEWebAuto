# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:25
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bba_suspension.py
# @Software: PyCharm

from action.commonAction import *
from appModules.am_disclosure.am_dealinstruc.am_suspension import suspensionAction
from util.Log import *
import unittest
from selenium import webdriver
from config.VarConfig import *
import ddt

url = testUrl+'/disclosure/dealinstruc/suspension/'

@ddt.ddt
class suspensionCase(unittest.TestCase):
    '''停复牌信息测试用例集合'''

    @ddt.data(['chrome','2018-09-12','18国债15'])
    @ddt.unpack
    def test_searchSuspensionByAllCondition(self,browserName,testData,expectData):
        '''通过全条件查询一般公告信息'''
        try:
            logging.info('场景：停复牌信息测试场景 测试开始。。。')
            launchBrowser(browserName,url)
            suspensionAction.searchSuspensionByAllCondition(webdriver,testData)
            assertPageElement(expectData)
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()