# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 10:19
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : pageAction.py
# @Software: PyCharm

from util.ObjectMap import *
from util.DirAndTime import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config.VarConfig import *
from selenium.webdriver.support.ui import Select

driver = None

def open_browser(browserName,*arg):
    '''
    打开浏览器
    :param browserName:浏览器名称
    '''
    global driver
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path= ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            chrome_options = Options()
            chrome_options.add_experimental_option('excludeSwitches',['Chrome 正受到自动测试软件的控制'])
            driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            driver = webdriver.Firefox(executable_path= fireFoxDriverFilePath)
    except Exception as e:
        raise e

def visit_url(url,*arg):
    '''
    访问url
    :param url:被访问的url
    '''
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*arg):
    '''
    关闭浏览器
    '''
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e


def sleep(sleepSeconds,*arg):
    '''
    暂停
    :param sleepSeconds:暂停秒数
    '''
    global driver
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e


def clear(locateType,locatorExpression):
    '''
    清除元素
    :param locateType:定位表达式
    :param locatorExpression:元素表达式
    '''
    global driver
    try:
        # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        # element.clear()
        getElement(locateType,locatorExpression).clear()
    except Exception as e:
        raise e


def input_string(locateType,locatorExpression,inputContent):
    '''
    输入内容
    :param locateType:定位表达式
    :param locatorExpression:元素表达式
    :param inputContent:输入内容
    '''
    global driver
    try:
        # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        # element.send_keys(inputContent)
        getElement(locateType,locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(locateType,locatorExpression,*arg):
    '''
    点击
    :param locateType:定位表达式
    :param locatorExpression:元素表达式
    '''
    global driver
    try:
        # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        # element.click()
        getElement(locateType,locatorExpression).click()
    except Exception as e:
        raise e

def capture_screen(*args):
    '''截图'''
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(createCurrentDateDir()) + '\\' + str(currTime) + '.png'
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('\\', r'\\'))
    except Exception as e:
        raise e


def assert_string_in_pageSource(assertString,*arg):
    '''验证页面元素
    :param:assertString:预期文字
    '''
    global driver
    try:
        assert assertString in driver.page_source,'%s not found in page source!'%assertString
    except AssertionError as e:
        capture_screen(driver)
        raise AssertionError(e)
    except Exception as e:
        raise e


def operate_window_handle():
    '''
    窗口跳转处理
    '''
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
    '''窗口最大化'''
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

def get_title():
    '''获取标题'''
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

def selectByValue(locateType,locatorExpression,value,*arg):
    '''
    通过value值选择
    :param locateType:定位表达式
    :param locatorExpression:元素表达式
    :param value:选择值
    '''
    global driver
    try:
        # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        elementObj = getElement(locateType,locatorExpression)
        Select(elementObj).select_by_value(value)
    except Exception as e:
        raise e

def js(script):
    '''
    js
    :param script:脚本
    '''
    global driver
    try:
        driver.execute_script(script)
    except Exception as e:
        raise e

if __name__ == "__main__":
    from selenium import webdriver
    