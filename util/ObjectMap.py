# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:03
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ObjectMap1.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium import webdriver
from config.VarConfig import *
import time
from util.DirAndTime import *
from selenium.webdriver.chrome.options import Options

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
    # 打开浏览器
    global driver
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path= ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            chrome_options = Options()
            chrome_options.add_experimental_option('excludeSwitches',[''])
            driver = webdriver.Chrome(chrome_options=chrome_options)
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

def capture_screen(*args):
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(createCurrentDateDir()) + '\\' + str(currTime) + '.png'
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('\\', r'\\'))
    except Exception as e:
        raise e


def assert_string_in_pageSource(assertString,*arg):
    global driver
    try:
        assert assertString in driver.page_source,'%s not found in page source!'%assertString
    except AssertionError as e:
        driver.capture_screen()
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

def selectByValue(locateType,locatorExpression,value,*arg):
    global driver
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        Select(element).select_by_value(value)
    except Exception as e:
        raise e

def js(script):
    global driver
    try:
        driver.execute_script(script)
    except Exception as e:
        raise e


