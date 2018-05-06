# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:08
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : EnterAnnouncementPage.py
# @Software: PyCharm

from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class enterAnnouncementPage(object):
    # url='http://www.sse.com.cn'

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.announcementOptions = self.parseCF.getItemsSection('announcement_leftMenuPage')
        print(self.announcementOptions)

    def openSSE(self,url):
        try:
            openBrowser(self.driver,url)
        except Exception as e:
            raise e

    def disclosureObj(self):
        try:
            locateType,locatorExpression = self.announcementOptions['leftMenuPage.disclosure'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def listedinfoObj(self):
        try:
            locateType,locatorExpression = self.announcementOptions['leftMenuPage.listedinfo'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementObj(self):
        try:
            locateType,locatorExpression = self.announcementOptions['leftMenuPage.announcement'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
