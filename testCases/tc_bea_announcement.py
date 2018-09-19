# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 14:10
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bea_announcement.py
# @Software: PyCharm

from selenium import webdriver
from appModules.am_disclosure.am_listedinfo.am_announcement import announcementAction
from testScripts.ts_disclosure.ts_listedinfo.ts_announcement import *
from util.Log import *
import unittest


class announcementCase(unittest.TestCase):
    '''最新公告测试用例'''

    def test_searchAnnouncementByAllCondition(self):
        '''通过全部查询条件查询最新公告'''
        try:
            logging.info('场景：最新公告页面通过全部条件查询公告测试开始。。。')
            announcementAction.LaunchBrowser('chrome','http://www.sse.com.cn/disclosure/listedinfo/announcement/')
            announcementAction.searchAnnouncementByAllCondition(webdriver,'600000','浦发银行','DQGG','2018-04-01',
                                                                '2018-05-07','浦发银行2018年第一季度报告')
        except Exception as e:
            raise e
    # test_searchAnnouncementByAllCondition()
if __name__ == '__main__':
    unittest.main()



