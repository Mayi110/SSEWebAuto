# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 9:11
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_detail.py
# @Software: PyCharm

from pageObjects.po_market.po_othersdata.po_margin.po_detail import detailPage
from util.Log import *
from util.ObjectMap import *


class detailAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchDetailByAllCondition(driver,companyCode,startDate):
        try:
            DP = detailPage(driver)

            logging.info('输入公司代码或者简称：%s'%companyCode)
            DP.companyCodeObj().send_keys(companyCode)
            sleep(1)

            logging.info('清除日期输入框存在的日期')
            DP.startDateObj().clear()
            sleep(1)

            logging.info('选择日期：%s'%startDate)
            DP.startDateObj().send_keys(startDate)
            sleep(1)

            logging.info('单击查询按钮')
            DP.searchButtonObj().click()
            sleep(5)
        except Exception as e:
            raise e