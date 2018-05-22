# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 15:57
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_promisho.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *


class promishoPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('promishoPage')

    def inputBoxObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['promishoPage.inputCode'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def promiseMainNameObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['promishoPage.promiseMainName'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def promiseTypeObj(self,value):
        try:
            javascript="document.getElementById('single_select_dyn_0').style.display='block';"
            js(javascript)
            locateType,locatorExpression = self.searchOptions['promishoPage.promiseType'.lower()].split('>')
            elementObj = selectByValue(locateType, locatorExpression,value)
            return elementObj
        except Exception as e:
            raise e

    def itemTypeObj(self,value):
        try:
            javascript="document.getElementById('single_select_dyn_1').style.display='block';"
            js(javascript)
            locateType,locatorExpression = self.searchOptions['promishoPage.itemType'.lower()].split('>')
            elementObj = selectByValue(locateType, locatorExpression,value)
            return elementObj
        except Exception as e:
            raise e

    def promiseStatusObj(self,value):
        try:
            javascript="document.getElementById('single_select_dyn_2').style.display='block';"
            js(javascript)
            locateType,locatorExpression = self.searchOptions['promishoPage.promiseStatus'.lower()].split('>')
            elementObj = selectByValue(locateType, locatorExpression,value)
            return elementObj
        except Exception as e:
            raise e

    def searchButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['promishoPage.btnQuery'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def linkObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['promishoPage.link'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e