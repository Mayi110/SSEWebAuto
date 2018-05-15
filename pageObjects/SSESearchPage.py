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

    def searchButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.submitButton'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def assertWebSWDPageElementObj(self):
        try:
           locateType,locatorExpression = self.searchOptions['searchPage.verifyWebswd'.lower()].split('>')
           elementObj=assertKeyWord(self.driver,locateType,locatorExpression)
           return elementObj
        except Exception as e:
            raise e

    def assertAnnouncementPageElementObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.verifyWebswd'.lower()].split('>')
            getText(self.driver,locateType,locatorExpression)
        except Exception as e:
            raise e

    def linkObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.submitButton'.lower()].split('>')
            elementObj = list_link(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def switchWindowObj(self):
        try:
            operateWindowHandle(self.driver)
        except Exception as e:
            raise e


if __name__ == '__main__':
    sseSearchPage.assertAnnouncementPageElementObj()




