# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 10:45
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_regular.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_listedinfo.po_regular import regularPage
from util.Log import *
from util.ObjectMap import *


class regularAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchRegularByAllCondition(driver,companyCode,type,startDate,endDate):
        try:
            RP = regularPage(driver)

            logging.info('输入公司代码或者简称：%s'%companyCode)
            RP.companyCodeObj().send_keys(companyCode)
            sleep(1)

            logging.info('选择的公告类型是：%s'%type)
            RP.announcementTypeObj(type)
            sleep(1)

            logging.info('选择开始日期：%s'%startDate)
            RP.announcementStartDateObj().send_keys(startDate)

            logging.info('选择结束日期：%s'%endDate)
            RP.announcementEndDateObj().send_keys(endDate)
            sleep(1)

            logging.info('单击查询按钮')
            RP.searchButtonObj().click()
            sleep(5)

            logging.info('单击第一条公告链接')
            RP.announcementLinkObj().click()
            sleep(5)
        except Exception as e:
            raise e