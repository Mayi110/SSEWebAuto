# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:03
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ObjectMap.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait

driver = None

def getElement(locateType,locatorExpression):
    '''
    获取单个元素对象
    :param locateType:定位表达式
    :param locatorExpression;元素表达式
    '''
    global driver
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e


def getElements(locateType,locatorExpression):
    '''
    获取多个元素对象
    :param locateType:定位表达式
    :param locatorExpression;元素表达式
    '''
    try:
        global driver
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locateType, value=locatorExpression))
        return elements
    except Exception as e:
        raise e


# def getItemsSection(self,itemsSection):
#     self.parseCF = ParseConfigFile()
#     self.searchOptions = self.parseCF.getItemsSection(itemsSection)
#
# def getOptions(self,Options):
#     try:
#         locateType,locatorExpression = self.searchOptions[Options.lower()].split('>')
#         elementObj = getElement(locateType, locatorExpression)
#         return elementObj
#     except Exception as e:
#         raise e





