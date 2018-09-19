# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 13:58
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_periodic.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_listedinfo.po_periodic import periodicPage
from pageObjects.po_common.po_commonPage import commonPage
from util.Log import *
from util.ObjectMap import *


class periodicAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchPeriodicByAllConditionAndEnterRegularPage(driver,companyCode):
        try:
            CP = commonPage(driver)

            # logging.info('选择的公告类型是：%s'%type)
            # CP.announcementTypeObj(type)
            # sleep(1)

            logging.info('清空公司代码或者简称输入框内容')
            CP.inputCodeObj().clear()
            sleep(1)

            logging.info('输入公司代码或者简称：%s'%companyCode)
            CP.inputCodeObj().send_keys(companyCode)
            sleep(1)

            # logging.info('清空日期内容')
            # CP.singleDate().clear()
            #
            # logging.info('选择日期：%s'%singleDate)
            # CP.singleDate().send_keys(singleDate)

            logging.info('单击查询按钮')
            CP.searchButtonObj().click()
            sleep(5)

            PP = periodicPage(driver)

            logging.info('点击 实际披露日 链接')
            PP.actualDateLinkObj().click()
            sleep(5)
        except Exception as e:
            raise e

    @staticmethod
    def searchPeriodicByAllConditionAndEnterCompanyInfoPage(driver,companyCode):
        try:
            PP = periodicPage(driver)
            CP = commonPage(driver)

            # logging.info('选择的公告类型是：%s'%type)
            # CP.announcementTypeObj(type)
            # sleep(1)

            logging.info('清空公司代码或者简称输入框内容')
            CP.inputCodeObj().clear()
            sleep(1)

            logging.info('输入公司代码或者简称：%s'%companyCode)
            CP.inputCodeObj().send_keys(companyCode)
            sleep(1)

            # logging.info('清空日期内容')
            # CP.singleDate().clear()
            #
            # logging.info('选择日期：%s'%singleDate)
            # CP.singleDate().send_keys(singleDate)

            logging.info('单击查询按钮')
            CP.searchButtonObj().click()
            sleep(5)

            logging.info('点击 公司代码 链接')
            PP.companyCodeLinkObj().click()
            sleep(5)
        except Exception as e:
            raise e