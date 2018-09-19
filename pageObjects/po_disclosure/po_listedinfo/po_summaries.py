# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 10:22
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_summaries.py
# @Software: PyCharm

from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class summariesPage(object):
    '''公告摘要页面'''

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.regularOptions = self.parseCF.getItemsSection('summariesPage')

    def announcementLinkObj(self):
        try:
            locateType,locatorExpression = self.regularOptions['summariesPage.announcementLink'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e