# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 16:24
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : PageAction.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time
from config.VarConfig import ieDriverFilePath
from config.VarConfig import fireFoxDriverFilePath
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


driver = None
waitUtil = None

def open_browser(browserName,*arg):
    global driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path= ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox(executable_path= fireFoxDriverFilePath)
        waitUtil = WaitUtil(driver)
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
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

def select(driver,locateType,locatorExpression,value):
    try:
        element = driver.getElement(locateType,locatorExpression)
        Select(element).select_by_value(value)
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

def js(driver,script):
    try:
        driver.execute_script(script)
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

def list_link(driver,locateType,locatorExpression):
    try:
        element = driver.getElement(locateType,locatorExpression)
        ActionChains(driver).move_to_element(element).perform()
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
