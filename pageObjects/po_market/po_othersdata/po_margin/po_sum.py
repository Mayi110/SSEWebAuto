# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 9:11
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_sum.py
# @Software: PyCharm

from action.pageAction import *


class sumPage(object):

    def __init__(self,driver):
        self.driver = driver
        # self.parseCF = ParseConfigFile()
        # self.searchOptions = self.parseCF.getItemsSection('sumPage')
        getItemsSection(self,'sumPage')

    def companyCodeObj(self,value,inputContent):
        # try:
        #     locateType,locatorExpression = self.searchOptions['sumPage.inputCode'.lower()].split('>')
        #     elementObj = getElement(self.driver,locateType,locatorExpression)
        #     return elementObj
        # except Exception as e:
        #     raise e
        # operateInputBox(self,value,'sumPage.inputCode',inputContent)
        getOptions(self,'sumPage.inputCode')


    def startDateObj(self,inputContent):
        javascript = 'document.getElementById("start_date").removeAttribute("readonly");'
        js(javascript)
        getOptions(self,'sumPage.startDate')
        # try:
        #     javascript = 'document.getElementById("start_date").removeAttribute("readonly");'
        #     js(javascript)
        #     locateType,locatorExpression = self.searchOptions['sumPage.startDate'.lower()].split('>')
        #     elementObj = getElement(self.driver,locateType,locatorExpression)
        #     return elementObj
        # except Exception as e:
        #     raise e
        # operateJS(self,javascript,'sumPage.startDate',inputContent)

    def endDateObj(self,inputContent):
        javascript = 'document.getElementById("end_date").removeAttribute("readonly");'
        js(javascript)
        getOptions(self,'sumPage.endDate')
        # try:
        #     javascript = 'document.getElementById("end_date").removeAttribute("readonly");'
        #     js(javascript)
        #     locateType,locatorExpression = self.searchOptions['sumPage.endDate'.lower()].split('>')
        #     elementObj = getElement(self.driver,locateType,locatorExpression)
        #     return elementObj
        # except Exception as e:
        #     raise e
        # operateJS(self,javascript,'sumPage.endDate',inputContent)

    def searchButtonObj(self):
        # try:
        #     locateType,locatorExpression = self.searchOptions['sumPage.btnQuery'.lower()].split('>')
        #     elementObj = getElement(self.driver,locateType,locatorExpression)
        #     return elementObj
        # except Exception as e:
        #     raise e
        # clickButton(self,'sumPage.btnQuery')
        getOptions(self,'sumPage.btnQuery')
