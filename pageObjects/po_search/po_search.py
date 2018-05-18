# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 14:37
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_search.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *


class sseSearchPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('sse_searchPage')

    def inputBoxObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.inputBox'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def searchButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.submitButton'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def companyCodeLinkObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.companyCodeLink'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e



