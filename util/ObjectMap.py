# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:03
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ObjectMap1.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from config.VarConfig import *
import time

driver = None

# 获取单个页面元素对象
def getElement(locateType,locatorExpression):
    global driver
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e


# 获取多个页面元素对象
def getElements(locateType,locatorExpression):
    '''
    启动浏览器
    :param url:测试地址
    :param 在启动时设置浏览器的类型
    '''
    global driver
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locateType, value=locatorExpression))
        return elements
    except Exception as e:
        raise e

def open_browser(browserName,*arg):
    global driver
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path= ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox(executable_path= fireFoxDriverFilePath)
    except Exception as e:
        raise e

def visit_url(url,*arg):
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*arg):
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e


def sleep(sleepSeconds,*arg):
    global driver
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e


def clear(locateType,locatorExpression):
    global driver
    try:
        element = driver.getElement(locateType,locatorExpression)
        element.clear()
    except Exception as e:
        raise e


def input_string(locateType,locatorExpression,inputContent):
    global driver
    try:
        element = driver.getElement(locateType,locatorExpression)
        element.send_keys(inputContent)
    except Exception as e:
        raise e

def click(locateType,locatorExpression,*arg):
    global driver
    try:
        element = driver.getElement(locateType,locatorExpression)
        element.click()
    except Exception as e:
        raise e


def assert_string_in_pageSource(assertString,*arg):
    global driver
    try:
        assert assertString in driver.page_source,'%s not found in page source!'%assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e


def operate_window_handle():
    global driver
    try:
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
    except Exception as e:
        raise e


def maximize_browser():
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

def get_title():
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

