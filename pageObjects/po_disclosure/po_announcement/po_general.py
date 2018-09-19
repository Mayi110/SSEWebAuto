# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 13:37
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_general.py
# @Software: PyCharm

from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class generalPage(object):
    '''一般公告页面'''

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.regularOptions = self.parseCF.getItemsSection('generalPage')

    def announcementLinkObj(self):
        try:
            locateType,locatorExpression = self.regularOptions['generalPage.announcementLink'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e