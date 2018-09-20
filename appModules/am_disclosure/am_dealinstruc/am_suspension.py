# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:18
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_suspension.py
# @Software: PyCharm


from pageObjects.po_disclosure.po_announcement.po_general import generalPage
from pageObjects.po_common.po_commonPage import commonPage
from util.Log import *
from util.ObjectMap import *


class suspensionAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchSuspensionByAllCondition(driver,date):
        try:
            CP = commonPage(driver)

            logging.info('清除日期')
            CP.singleDate().clear()
            sleep(1)

            logging.info('选择查询日期')
            CP.singleDate().send_keys(date)
            sleep(1)

            logging.info('单击查询按钮')
            CP.searchButtonObj().click()
            sleep(10)
        except Exception as e:
            raise e