# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:33
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_listing.py
# @Software: PyCharm

from appModules.am_disclosure.am_listedinfo.am_listing import listingAction
from util.Log import *
import unittest
from action.commonAction import *
from selenium import webdriver
from time import sleep


class listingCase(unittest.TestCase):
    '''发行上市公告测试用例'''

    def test_searchListingAnnouncementByAllCondition(self):
        '''通过全部查询条件查询发行上市公告'''
        try:
            logging.info('场景：发行上市公告页面通过全部条件查询公告测试开始。。。')
            launchBrowser('chrome','http://www.sse.com.cn/disclosure/listedinfo/listing/')
            sleep(5)
            listingAction.searchRegularByAllCondition(webdriver,'600010','2018-05-09',
                                                                '2018-05-23')
            closeBrowser()
        except Exception as e:
            raise e
if __name__ == '__main__':
    unittest.main()