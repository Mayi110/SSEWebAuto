# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:56
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_announcement.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *


class announcementPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('announcementPage')

    def companyCodeObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['announcementPage.inputCode'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def keyWordObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['announcementPage.keyWord'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementTypeObj(self,value):
        try:
            javascript="document.getElementById('single_select_2').style.display='block';"
            js(javascript)
            locateType,locatorExpression = self.searchOptions['announcementPage.announcementType'.lower()].split('>')
            elementObj = selectByValue(locateType,locatorExpression,value)
            return elementObj
        except Exception as e:
            raise e

    def announcementStartDateObj(self):
        try:
            javascript = 'document.getElementById("start_date").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.searchOptions['announcementPage.startDate'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementEndDateObj(self):
        try:
            javascript = 'document.getElementById("end_date").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.searchOptions['announcementPage.endDate'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def searchButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['announcementPage.btnQuery'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementLinkObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['announcementPage.announcementLink'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementCloseObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['announcementPage.announcementClose'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
