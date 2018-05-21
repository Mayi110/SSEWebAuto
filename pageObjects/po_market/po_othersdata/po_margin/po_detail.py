# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 9:11
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_detail.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *
from action.pageAction import *


class detailPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('detailPage')

    def companyCodeObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['detailPage.inputCode'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e


    def startDateObj(self):
        try:
            javascript = 'document.getElementById("start_date2").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.searchOptions['detailPage.startDate'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e


    def searchButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['detailPage.btnQuery'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e