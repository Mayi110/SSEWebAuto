# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 14:51
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_change.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_credibility.po_supervision.po_change import changePage
from pageObjects.po_common.po_commonPage import commonPage
from util.Log import *
from util.ObjectMap import *


class changeAction(object):
    def __init__(self):
        print('sseSearch....')

    @staticmethod
    def searchChangeByAll(driver,companyCode,userName,startDate,endDate):
        try:
            CHP = changePage(driver)
            CP = commonPage(driver)

            logging.info('清除公司代码或简称输入框的内容')
            CP.inputCodeObj().clear()
            sleep(1)

            logging.info('输入公司代码：%s'%companyCode)
            CP.inputCodeObj().send_keys(companyCode)
            sleep(2)

            logging.info('清除姓名输入框的内容')
            CHP.userNameInputObj().clear()
            sleep(1)

            logging.info('填写的用户姓名是：%s'%userName)
            CHP.userNameInputObj().send_keys(userName)
            sleep(2)

            logging.info('清除开始日期存在的内容')
            CP.startDateObj().clear()
            sleep(1)

            logging.info('选择开始日期：%s'%startDate)
            CP.startDateObj().send_keys(startDate)
            sleep(1)

            logging.info('清除结束日期存在的内容')
            CP.endDateObj().clear()
            sleep(1)

            logging.info('选择结束日期：%s'%endDate)
            CP.endDateObj().send_keys(endDate)
            sleep(1)

            logging.info('点击查询按钮')
            CP.searchButtonObj().click()
            sleep(5)

            logging.info('点击公司code链接')
            CHP.companyCodeLinkObj().click()
            sleep(5)

            logging.info('获取当前窗口的标题:%s'%get_title())
        except Exception as e:
            raise e