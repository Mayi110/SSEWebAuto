# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 14:14
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_change.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *


class changePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('changePage')

    def userNameInputObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['changePage.userNameInput'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def companyCodeLinkObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['changePage.companyCodeLink'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e