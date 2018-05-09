# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 16:30
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : BaseObjectMap.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver

OVER_TIME=5
BASE_URL='http://www.sse.com.cn'

class BasePage(object):

    def Browser(self,url=BASE_URL,driver_name='Chrome'):
        '''
        启动浏览器
        :param url:测试地址
        :param 在启动时设置浏览器的类型
        '''
        if driver_name == 'Chrome':
            self.driver = webdriver.Chrome()
        elif driver_name == 'ff':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Ie()
        self.driver.implicitly_wait(OVER_TIME)
        self.driver.get(url)
        self.driver.maximize_window()

    def get_url(self):
        try:
            return BASE_URL
        except Exception as e:
            raise e

    def getElement(self,locateType,locatorExpression):
        '''
        获取单个页面元素对象
        :param locateType:元素定位器
        :param locatorExpression:元素表达式
        '''
        try:
            element = WebDriverWait(self.driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
            return element
        except Exception as e:
            raise e


    def getElements(driver,locateType,locatorExpression):
        '''
        获取多个页面元素对象
        :param locateType:元素定位器
        :param locatorExpression:元素表达式
        '''
        try:
            elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locateType, value=locatorExpression))
            return elements
        except Exception as e:
            raise e


    def getDropListByValue(driver,locateType,locatorExpression,value):
        try:
            elements = Select(WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locateType, value=locatorExpression)))
            all_options = elements.options
            if all_options(value).is_enabled() and all_options(value).is_selected():
                select_elements=elements.select_by_value(value)
                print(select_elements.text)
                return select_elements
        except Exception as e:
            raise e

    def close(self):
        '''
        关闭浏览器
        '''
        self.driver.close()

    def quit(self):
        '''
        退出浏览器
        '''
        self.driver.quit()