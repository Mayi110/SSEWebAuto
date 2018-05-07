# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:56
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SearchAnnouncementPage.py
# @Software: PyCharm

from selenium import webdriver
import unittest
from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *


class searchAnnouncementPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('announcement_searchPage')
        print(self.searchOptions)

    def companyCodeObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.companyCode'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def keyWordObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.keyWord'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementTypeObj(self,value):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.announcementType'.lower()].split('>')
            elementObj = getDropListByValue(self.driver,locateType,locatorExpression,value)
            return elementObj
        except Exception as e:
            raise e

    def announcementStartDateObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.announcementStartDate'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementEndDateObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.announcementEndDate'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def searchButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.searchButton'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementLinkObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.announcementLink'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementCloseObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.announcementClose'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()