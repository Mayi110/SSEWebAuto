# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 9:11
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_sum.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *


class sumPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('sumPage')

    def companyCodeObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['sumPage.inputCode'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e


    def startDateObj(self):
        try:
            javascript = 'document.getElementById("start_date").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.searchOptions['sumPage.startDate'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def endDateObj(self):
        try:
            javascript = 'document.getElementById("end_date").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.searchOptions['sumPage.endDate'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def searchButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['sumPage.btnQuery'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
