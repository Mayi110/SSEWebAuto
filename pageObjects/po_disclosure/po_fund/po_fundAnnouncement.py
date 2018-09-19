# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 15:53
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_fundAnnouncement.py
# @Software: PyCharm

from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class fundAnnouncementPage(object):
    '''最新基金公告页面'''

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.regularOptions = self.parseCF.getItemsSection('fundAnnouncementPage')

    def fundAnnouncementLinkObj(self):
        try:
            locateType,locatorExpression = self.regularOptions['fundAnnouncementPage.fundAnnouncementLink'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
