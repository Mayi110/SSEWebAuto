# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:33
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_beb_listing.py
# @Software: PyCharm

from appModules.am_disclosure.am_listedinfo.am_listing import listingAction
from util.Log import *
import unittest
from action.commonAction import *
from selenium import webdriver
import ddt

url = testUrl+'/disclosure/listedinfo/listing/'

@ddt.ddt
class listingCase(unittest.TestCase):
    '''发行上市公告测试用例'''

    @ddt.data(['chrome','600010','2018-05-09','2018-05-23'])
    @ddt.unpack
    def test_searchListingAnnouncementByAllCondition(self,browserName,code,startDate,endDate):
        '''通过全部查询条件查询发行上市公告'''
        try:
            logging.info('场景：发行上市公告页面通过全部条件查询公告测试开始。。。')
            launchBrowser(browserName,url)
            sleep(5)
            listingAction.searchListingByAllCondition(webdriver,code,startDate,endDate)
            closeBrowser()
        except Exception as e:
            raise e
if __name__ == '__main__':
    unittest.main()