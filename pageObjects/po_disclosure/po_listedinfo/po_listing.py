# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:11
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_listing.py
# @Software: PyCharm

from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class listingPage(object):
    '''发行上市公告页面'''

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        # self.commonOptions = self.parseCF.getItemsSection('commonPage')
        self.regularOptions = self.parseCF.getItemsSection('listingPage')

    # def companyCodeObj(self):
    #     try:
    #         locateType,locatorExpression = self.commonOptions['commonPage.inputCode'.lower()].split('>')
    #         elementObj = getElement(locateType,locatorExpression)
    #         return elementObj
    #     except Exception as e:
    #         raise e
    #
    # def announcementStartDateObj(self):
    #     try:
    #         javascript = 'document.getElementById("start_date").removeAttribute("readonly");'
    #         js(javascript)
    #         locateType,locatorExpression = self.commonOptions['commonPage.startDate'.lower()].split('>')
    #         elementObj = getElement(locateType,locatorExpression)
    #         return elementObj
    #     except Exception as e:
    #         raise e
    #
    # def announcementEndDateObj(self):
    #     try:
    #         javascript = 'document.getElementById("end_date").removeAttribute("readonly");'
    #         js(javascript)
    #         locateType,locatorExpression = self.commonOptions['commonPage.endDate'.lower()].split('>')
    #         elementObj = getElement(locateType,locatorExpression)
    #         return elementObj
    #     except Exception as e:
    #         raise e

    # def searchButtonObj(self):
    #     try:
    #         locateType,locatorExpression = self.commonOptions['commonPage.btnQuery'.lower()].split('>')
    #         elementObj = getElement(locateType,locatorExpression)
    #         return elementObj
    #     except Exception as e:
    #         raise e

    def announcementLinkObj(self):
        try:
            locateType,locatorExpression = self.regularOptions['listingPage.announcementLink'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e