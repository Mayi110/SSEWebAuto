# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 10:29
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_summaries.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_listedinfo.po_summaries import summariesPage
from pageObjects.po_common.po_commonPage import commonPage
from util.Log import *
from util.ObjectMap import *


class summariesAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchSummariesByAllCondition(driver,companyCode,startDate,endDate):
        try:
            CP = commonPage(driver)

            logging.info('清空公司代码或者简称输入框内容')
            CP.inputCodeObj().clear()
            sleep(1)

            logging.info('输入公司代码或者简称：%s'%companyCode)
            CP.inputCodeObj().send_keys(companyCode)
            sleep(1)

            logging.info('清空开始日期内容')
            CP.startDateObj().clear()

            logging.info('选择开始日期：%s'%startDate)
            CP.startDateObj().send_keys(startDate)

            logging.info('清空结束日期内容')
            CP.endDateObj().clear()

            logging.info('选择结束日期：%s'%endDate)
            CP.endDateObj().send_keys(endDate)
            sleep(1)

            logging.info('单击查询按钮')
            CP.searchButtonObj().click()
            sleep(5)

            PP = summariesPage(driver)

            logging.info('点击 公告 链接')
            PP.announcementLinkObj().click()
            sleep(5)
        except Exception as e:
            raise e