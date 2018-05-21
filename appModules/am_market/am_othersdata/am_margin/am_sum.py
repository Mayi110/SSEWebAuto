# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 9:11
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_sum.py
# @Software: PyCharm

from pageObjects.po_market.po_othersdata.po_margin.po_sum import sumPage
from util.Log import *
from util.ObjectMap import *
from action.pageAction import *


class sumAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchSumByAllCondition(driver,companyCode,startDate,endDate):
        try:
            SP = sumPage(driver)

            logging.info('输入公司代码或者简称：%s'%companyCode)
            SP.companyCodeObj().send_keys(companyCode)
            sleep(1)

            logging.info('清除开始日期输入框存在的日期')
            SP.startDateObj().clear()
            sleep(1)

            logging.info('选择开始日期：%s'%startDate)
            SP.startDateObj().send_keys(startDate)
            sleep(1)

            logging.info('清除结束日期输入框存在的日期')
            SP.endDateObj().clear()
            sleep(1)

            logging.info('选择结束日期：%s'%endDate)
            SP.endDateObj().send_keys(endDate)
            sleep(1)

            logging.info('单击查询按钮')
            SP.searchButtonObj().click()
            sleep(5)
        except Exception as e:
            raise e