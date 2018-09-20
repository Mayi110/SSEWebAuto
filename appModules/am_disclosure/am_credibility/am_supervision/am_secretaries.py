# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 16:36
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_secretaries.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_credibility.po_supervision.po_secretaries import secretariesPage
from pageObjects.po_common.po_commonPage import commonPage
from util.Log import *
from util.ObjectMap import *


class secretariesAction(object):
    def __init__(self):
        print('sseSearch....')


    @staticmethod
    def searchSecretariesByAll(driver,companyCode):
        try:
            SP = secretariesPage(driver)
            CP = commonPage(driver)

            logging.info('清除公司代码或简称输入框的内容')
            CP.inputCodeObj().clear()

            logging.info('输入公司代码：%s'%companyCode)
            CP.inputCodeObj().send_keys(companyCode)
            sleep(2)

            logging.info('点击查询按钮')
            CP.searchButtonObj().click()
            sleep(5)

            logging.info('点击公告链接')
            SP.codeLinkObj().click()
        except Exception as e:
            raise e