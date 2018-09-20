# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 16:33
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_secretaries.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *


class secretariesPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('secretariesPage')

    def codeLinkObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['secretariesPage.codeLink'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e