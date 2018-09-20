# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 16:21
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bdad_secretaries.py
# @Software: PyCharm

from action.commonAction import *
from appModules.am_disclosure.am_credibility.am_supervision.am_secretaries import secretariesAction
from util.Log import *
import unittest
import ddt

url = testUrl+'/disclosure/credibility/supervision/secretaries/'

@ddt.ddt
class secretariesCase(unittest.TestCase):
    '''董秘考核结果测试用例'''

    @ddt.data(['chrome','600000','公司概况'])
    @ddt.unpack
    def test_searchSecretariesByAllCondition(self,browserName,companyCode,expectData):
        '''通过全部查询条件查询最新公告'''
        try:
            logging.info('场景：董秘考核业务 测试开始。。。')
            launchBrowser(browserName,url)
            secretariesAction.searchSecretariesByAll(webdriver,companyCode)
            assertPageElement(expectData)
        except Exception as e:
            raise e
    # test_searchAnnouncementByAllCondition()
if __name__ == '__main__':
    unittest.main()