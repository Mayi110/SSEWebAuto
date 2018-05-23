# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:24
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_listing.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_listedinfo.po_listing import listingPage
from pageObjects.po_common.po_commonPage import commonPage
from util.Log import *
from util.ObjectMap import *


class listingAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchRegularByAllCondition(driver,companyCode,startDate,endDate):
        try:
            LP = listingPage(driver)
            CP = commonPage(driver)

            logging.info('输入公司代码或者简称：%s'%companyCode)
            CP.inputCodeObj().send_keys(companyCode)
            sleep(1)

            logging.info('清除开始日期框中存在的日期')
            CP.startDateObj().clear()
            sleep(1)

            logging.info('选择开始日期：%s'%startDate)
            CP.startDateObj().send_keys(startDate)
            sleep(1)

            logging.info('清除结束日期框中存在的日期')
            CP.endDateObj().clear()
            sleep(1)

            logging.info('选择结束日期：%s'%endDate)
            CP.endDateObj().send_keys(endDate)
            sleep(1)

            logging.info('单击查询按钮')
            CP.searchButtonObj().click()
            sleep(5)

            logging.info('单击第一条公告链接')
            LP.announcementLinkObj().click()
            sleep(5)
        except Exception as e:
            raise e