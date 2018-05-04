# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:03
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ObjectMap.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait


# 获取单个页面元素对象
def getElement(driver,locateType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e


# 获取多个页面元素对象
def getElements(driver,locateType,locatorExpression):
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locateType, value=locatorExpression))
        return elements
    except Exception as e:
        raise e