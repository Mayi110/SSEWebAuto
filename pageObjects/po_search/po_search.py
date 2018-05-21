# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 14:37
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : po_search.py
# @Software: PyCharm
from util.ParsePageElementFile import ParsePageElementFile
from util.ParseConfigurationFile import *
from util.ObjectMap import BasePage

class sseSearchPage(object):

    def __init__(self):
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection('sse_searchPage')
        # ParsePageElementFile.getItemsSection(self,'sse_searchPage')
        # self.driver = driver
        # self.parsePEF = ParsePageElementFile(driver)
        # self.parsePEF.getItemsSection('sse_searchPage')

    def inputBoxObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.inputBox'.lower()].split('>')
            elementObj = BasePage(driver).getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
        # inputBox = self.parsePEF.getOptions('searchPage.inputBox')
        # return inputBox


    def searchButtonObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.submitButton'.lower()].split('>')
            elementObj = BasePage(driver).getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
        # submitButton = self.parsePEF.getOptions('searchPage.submitButton')
        # return submitButton

    def companyCodeLinkObj(self):
        try:
            locateType,locatorExpression = self.searchOptions['searchPage.companyCodeLink'.lower()].split('>')
            elementObj = BasePage(driver).getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
        # companyCodeLink = self.parsePEF.getOptions('searchPage.companyCodeLink')
        # return companyCodeLink

if __name__ == "__main__":
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.sse.com.cn')
    sleep(2)
    sp = sseSearchPage(webdriver)
    sp.inputBoxObj().clear()
    sleep(2)
    sp.inputBoxObj().send_keys('浦发')
    sleep(2)
    sp.searchButtonObj().click()
    sleep(2)
    driver.quit()




