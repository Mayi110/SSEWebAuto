# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 14:38
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_inquiries.py
# @Software: PyCharm

from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *


class inquiriesPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('inquiriesPage')

    def inputBoxObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['inquiriesPage.inputCode'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def jglxObj(self,value):
        try:
            javascript="document.querySelectorAll('select')[0].style.display='block';"
            js(javascript)
            locateType,locatorExpression = self.searchOptions['inquiriesPage.ht_jglx'.lower()].split('>')
            elementObj = selectByValue(locateType, locatorExpression,value)
            return elementObj
        except Exception as e:
            raise e

    def startDateObj(self):
        try:
            javascript='document.getElementById("start_date").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.searchOptions['inquiriesPage.startDate'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def endDateObj(self):
        try:
            javascript='document.getElementById("end_date").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.searchOptions['inquiriesPage.endDate'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def searchButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['inquiriesPage.btnQuery'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def pdfLinkObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['inquiriesPage.PDFLink'.lower()].split('>')
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e