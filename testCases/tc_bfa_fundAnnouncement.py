# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 16:11
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bfa_fundAnnouncement.py
# @Software: PyCharm

from appModules.am_disclosure.am_fund.am_fundAnnouncement import fundAnnouncementAction
from util.Log import *
import unittest
from action.commonAction import *
from selenium import webdriver
from time import sleep
import ddt

url = testUrl+'/disclosure/fund/announcement/'

@ddt.ddt
class fundAnnouncementCase(unittest.TestCase):
    '''基金公告测试用例集合'''

    @ddt.data(['chrome','501023','lsgg','2018-09-15','2018-09-21'])
    @ddt.unpack
    def test_searchFundAnnouncementByAllCondition(self,browserName,companyCode,select,startDate,endDate):
        '''通过全部查询条件查询基金公告数据'''
        try:
            logging.info('场景：基金公告业务 测试开始。。。')
            launchBrowser(browserName,url)
            sleep(5)
            fundAnnouncementAction.searchFundAnnouncementByAll(webdriver,companyCode,select,startDate,endDate)
            sleep(5)
            closeBrowser()
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()