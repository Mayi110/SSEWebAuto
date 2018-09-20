# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 15:49
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_listing.py
# @Software: PyCharm

from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class listingPage(object):
    '''上市/退市公告页面'''

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.regularOptions = self.parseCF.getItemsSection('announcementListingPage')

    def listingLinkObj(self):
        try:
            locateType,locatorExpression = self.regularOptions['announcementListingPage.announcementLink'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e