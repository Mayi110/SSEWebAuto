# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 14:37
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SSESearchPage.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *


class sseSearchPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('sse_searchPage')
        print(self.searchOptions)

    def inputBoxObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.inputBox'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def seachButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.submitButton'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def assertPageElement(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.submitButton'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression).text
            return elementObj
        except Exception as e:
            raise e





