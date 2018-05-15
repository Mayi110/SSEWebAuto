# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 16:24
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : PageAction.py
# @Software: PyCharm

from selenium import webdriver
from util.WaitUtil import *
import time
from config.VarConfig import ieDriverFilePath
from config.VarConfig import fireFoxDriverFilePath
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,browserName,*arg):
        try:
            if browserName.lower() == 'ie':
                self.driver = webdriver.Ie(executable_path= ieDriverFilePath)
            elif browserName.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            else:
                self.driver = webdriver.Firefox(executable_path= fireFoxDriverFilePath)
            waitUtil = WaitUtil(self.driver)
        except Exception as e:
            raise e

    def visit_url(self,url,*arg):
        try:
            self.driver.get(url)
        except Exception as e:
            raise e

    def close_browser(self,*arg):
        try:
            self.driver.quit()
        except Exception as e:
            raise e


    def sleep(sleepSeconds,*arg):
        global driver
        try:
            time.sleep(int(sleepSeconds))
        except Exception as e:
            raise e


    def select(locateType,locatorExpression,value):
        global driver
        try:
            element = driver.getElement(locateType,locatorExpression)
            Select(element).select_by_value(value)
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


    def js(script):
        global driver
        try:
            driver.execute_script(script)
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


    def list_link(driver,locateType,locatorExpression):
        try:
            element = driver.getElement(locateType,locatorExpression)
            ActionChains(driver).move_to_element(element).perform()
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


    def maximaze_browser():
        global driver
        try:
            driver.maximize_window()
        except Exception as e:
            raise e