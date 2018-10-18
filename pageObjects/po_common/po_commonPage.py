# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:17
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_commonPage.py
# @Software: PyCharm

from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class commonPage(object):
    '''公共页面对象封装'''

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.commonOptions = self.parseCF.getItemsSection('commonPage')

    def inputCodeObj(self):
        '''代码或者简称输入框'''
        try:
            locateType,locatorExpression = self.commonOptions['commonPage.inputCode'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def keyWordObj(self):
        '''关键词输入框'''
        try:
            locateType,locatorExpression = self.commonOptions['commonPage.keyWord'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def announcementTypeObj(self,value):
        '''公告类型下拉选择框'''
        try:
            javascript="document.getElementById('single_select_2').style.display='block';"
            js(javascript)
            locateType,locatorExpression = self.commonOptions['commonPage.singleSelect2'.lower()].split('>')
            elementObj = selectByValue(locateType,locatorExpression,value)
            return elementObj
        except Exception as e:
            raise e

    def singleSelectObj(self,value):
        try:
            # javascript="document.getElementsByClassName('single_select').style.display='block';"
            javascript="document.querySelectorAll('select')[0].style.display='block';"
            js(javascript)
            locateType,locatorExpression = self.commonOptions['commonPage.singleSelect'.lower()].split('>')
            elementObj = selectByValue(locateType,locatorExpression,value)
            return elementObj
        except Exception as e:
            raise e

    def singleSelect2Obj(self,value):
        try:
            javascript="document.getElementById('single_select_2').style.display='block';"
            # javascript="document.querySelectorAll('select')[0].style.display='block';"
            js(javascript)
            locateType,locatorExpression = self.commonOptions['commonPage.singleSelect2'.lower()].split('>')
            elementObj = selectByValue(locateType,locatorExpression,value)
            return elementObj
        except Exception as e:
            raise e

    def startDateObj(self):
        '''开始日期选择框'''
        try:
            javascript = 'document.getElementById("start_date").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.commonOptions['commonPage.startDate'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def endDateObj(self):
        '''结束日期选择框'''
        try:
            javascript = 'document.getElementById("end_date").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.commonOptions['commonPage.endDate'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def searchButtonObj(self):
        '''查询按钮'''
        try:
            locateType,locatorExpression = self.commonOptions['commonPage.btnQuery'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def singleDate(self):
        '''单独选择日期'''
        try:
            javascript = 'document.getElementById("start_date2").removeAttribute("readonly");'
            js(javascript)
            locateType,locatorExpression = self.commonOptions['commonPage.singleDate'.lower()].split('>')
            elementObj = getElement(locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e