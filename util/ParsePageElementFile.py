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
    def  __init__(self,driver):
        self.driver = driver

    def getItemsSection(self,itemsSection):
        self.parseCF = ParseConfigFile()
        self.searchOptions = self.parseCF.getItemsSection(itemsSection)


    def getOptions(self,Options):
        try:
            locateType,locatorExpression = self.searchOptions[Options.lower()].split('>')
            # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType, value=locatorExpression))
            elementObj = getElement(self.driver,locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.baidu.com')
    pp = ParsePageElementFile(driver)
    aa = pp.getItemsSection('test')
    bb = pp.getOptions('test.case')
    searchBox = getElement(driver,aa,bb)
    print(searchBox.tag_name)
    driver.quit()



