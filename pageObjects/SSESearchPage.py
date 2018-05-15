# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 14:37
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SSESearchPage.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *
from action.PageAction import *


class sseSearchPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('sse_searchPage')
        print(self.searchOptions)


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
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def assertWebSWDPageElementObj(self,assertString):
        try:
            assert_string_in_pageSource(assertString)
        except Exception as e:
            raise e

    def assertAnnouncementPageElementObj(self,assertString):
        try:
            assert_string_in_pageSource(assertString)
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
            operate_window_handle()
        except Exception as e:
            raise e




