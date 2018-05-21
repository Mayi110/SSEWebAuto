# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 10:52
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ParsePageElementFile.py
# @Software: PyCharm

from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from selenium.webdriver.support.ui import WebDriverWait

class ParsePageElementFile(object):
    def  __init__(self):
        print('...')

    def getItemsSection(self,itemsSection):
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection(itemsSection)


    def getOptions(self,Options):
        try:
            locateType,locatorExpression = self.searchOptions[Options.lower()].split('>')
            # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType, value=locatorExpression))
            elementObj = getElement(locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
