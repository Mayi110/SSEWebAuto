# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 14:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SSESearchAction.py
# @Software: PyCharm

from pageObjects.SSESearchPage import sseSearchPage
from time import sleep


class sseSearchAction(object):
    def __init__(self):
        print('sseSearch....')

    @staticmethod
    def sseSearchByCompanyCode(driver,companyCode):
        SS = sseSearchPage(driver)

        SS.inputBoxObj().clear()
        SS.inputBoxObj().send_keys(companyCode)
        SS.seachButtonObj().click()
        sleep(8)
