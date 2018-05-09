# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:56
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SearchAnnouncementPage.py
# @Software: PyCharm

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

    def announcementTypeObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.announcementType'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementTypeOfDQGGObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.announcementTypeOfDQGG'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementStartDateObj(self):
        try:
            js = 'document.getElementById("start_date").removeAttribute("readonly");'
            self.driver.execute_script(js)
            locateType,locatorExpression = self.searchOptions['searchPage.announcementStartDate'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementEndDateObj(self):
        try:
            js = 'document.getElementById("end_date").removeAttribute("readonly");'
            self.driver.execute_script(js)
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
