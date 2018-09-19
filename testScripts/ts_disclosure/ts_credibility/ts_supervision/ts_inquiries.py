# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 15:06
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bdac_inquiries.py
# @Software: PyCharm

from appModules.am_disclosure.am_credibility.am_supervision.am_inquiries import inquiriesAction
from util.Log import *
from action.commonAction import *


def test_searchInquiriesByAllCondition():
    try:
        logging.info('场景：通过监管公司全条件查询，进入pdf页面 测试开始。。。')
        launchBrowser('chrome','http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/')
        inquiriesAction.searchMeasuresByAll(webdriver,'600086','定期报告事后审核意见函','2018-05-01','2018-05-17')
    except Exception as e:
        raise e
