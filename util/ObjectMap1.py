# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:03
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ObjectMap1.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from config.VarConfig import *

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

def open_browser(driver,browserName,*arg):
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path= ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox(executable_path= fireFoxDriverFilePath)
    except Exception as e:
        raise e

def visit_url(driver,url,*arg):
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(driver,*arg):
    try:
        driver.quit()
    except Exception as e:
        raise e


def sleep(driver,sleepSeconds,*arg):
    try:
        sleep(driver,int(sleepSeconds))
    except Exception as e:
        raise e


def clear(driver,locateType,locatorExpression):
    try:
        element = driver.getElement(locateType,locatorExpression)
        element.clear()
    except Exception as e:
        raise e


def input_string(driver,locateType,locatorExpression,inputContent):
    try:
        element = driver.getElement(locateType,locatorExpression)
        element.send_keys(inputContent)
    except Exception as e:
        raise e

def click(driver,locateType,locatorExpression,*arg):
    try:
        element = driver.getElement(locateType,locatorExpression)
        element.click()
    except Exception as e:
        raise e


def assert_string_in_pageSource(driver,assertString,*arg):
    try:
        assert assertString in driver.page_source,'%s not found in page source!'%assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e


def operate_window_handle(driver):
    try:
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
    except Exception as e:
        raise e


def maximize_browser(driver):
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

