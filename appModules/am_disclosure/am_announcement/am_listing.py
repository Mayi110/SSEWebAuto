# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 15:56
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_listing.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_announcement.po_listing import listingPage
from pageObjects.po_common.po_commonPage import commonPage
from util.Log import *
from util.ObjectMap import *


class listingAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchListingByAllCondition(driver,keyWord):
        try:
            CP = commonPage(driver)

            logging.info('清空关键字输入框内容')
            CP.keyWordObj().clear()
            sleep(1)

            logging.info('输入关键字：%s'%keyWord)
            CP.keyWordObj().send_keys(keyWord)
            sleep(1)

            logging.info('单击查询按钮')
            CP.searchButtonObj().click()
            sleep(5)

            operate_window_handle()
            logging.info('当前窗口的标题是:%s'%get_title())

            LP = listingPage(driver)

            logging.info('点击 公告 链接')
            LP.listingLinkObj().click()
            sleep(5)
        except Exception as e:
            raise e