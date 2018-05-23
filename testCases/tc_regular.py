# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 10:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_regular.py
# @Software: PyCharm

from appModules.am_disclosure.am_listedinfo.am_regular import regularAction
from util.Log import *
import unittest
from action.commonAction import *
from selenium import webdriver
from time import sleep


class regularCase(unittest.TestCase):
    '''定期公告测试用例'''

    def test_searchAnnouncementByAllCondition(self):
        '''通过全部查询条件查询定期公告'''
        try:
            logging.info('场景：最新公告页面通过全部条件查询公告测试开始。。。')
            launchBrowser('chrome','http://www.sse.com.cn/disclosure/listedinfo/regular/')
            sleep(5)
            regularAction.searchRegularByAllCondition(webdriver,'600165','YEARLY','2018-05-01',
                                                                '2018-05-23')
            closeBrowser()

        except Exception as e:
            raise e
if __name__ == '__main__':
    unittest.main()