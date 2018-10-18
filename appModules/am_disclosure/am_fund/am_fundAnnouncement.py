# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 16:10
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_fundAnnouncement.py
# @Software: PyCharm

from pageObjects.po_common.po_commonPage import commonPage
from pageObjects.po_disclosure.po_fund.po_fundAnnouncement import fundAnnouncementPage
from util.Log import *
from util.ObjectMap import *


class fundAnnouncementAction(object):
    def __init__(self):
        print('sseSearch....')

    @staticmethod
    def searchFundAnnouncementByAll(driver,companyCode,select,startDate,endDate):
        try:
            CP = commonPage(driver)
            FP = fundAnnouncementPage(driver)

            logging.info('清除公司代码或简称输入框的内容')
            CP.inputCodeObj().clear()

            logging.info('输入公司代码：%s'%companyCode)
            CP.inputCodeObj().send_keys(companyCode)
            sleep(2)

            logging.info('选择基金公告类型：%s'%select)
            CP.singleSelect2Obj(select)
            sleep(2)

            logging.info('输入开始时间：%s'%startDate)
            CP.startDateObj().send_keys(startDate)
            sleep(2)

            logging.info('输入结束时间：%s'%endDate)
            CP.endDateObj().send_keys(endDate)
            sleep(2)

            logging.info('单击查询按钮')
            CP.searchButtonObj().click()
            sleep(5)

            logging.info('点击基金信息公告链接')
            FP.fundAnnouncementLinkObj().click()
            sleep(8)
        except Exception as e:
            raise e







