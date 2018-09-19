# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 13:54
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_periodic.py
# @Software: PyCharm

from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class periodicPage(object):
    '''定期报告预约情况页面'''

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.regularOptions = self.parseCF.getItemsSection('periodicPage')

    def companyCodeLinkObj(self):
        try:
            locateType,locatorExpression = self.regularOptions['periodicPage.companyCodeLink'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def actualDateLinkObj(self):
        try:
            locateType,locatorExpression = self.regularOptions['periodicPage.actualDateLink'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e