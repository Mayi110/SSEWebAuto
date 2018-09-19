# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 16:36
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ts_fundAnnouncement.py
# @Software: PyCharm

from appModules.am_disclosure.am_fund.am_fundAnnouncement import fundAnnouncementAction
from util.Log import *
from action.commonAction import *

def test_searchFundAnnouncementByAllCondition():
    try:
        logging.info('场景：通过最新基金公告全条件查询，进入pdf页面 测试开始。。。')
        launchBrowser('chrome','http://www.sse.com.cn/disclosure/fund/announcement/')
        fundAnnouncementAction.searchFundAnnouncementByAll(webdriver,'501303','lsgg','2018-09-15','2018-09-18')
    except Exception as e:
        raise e