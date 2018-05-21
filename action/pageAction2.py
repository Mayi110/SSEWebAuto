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


class basePage(object):
    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,browserName,*arg):
        '''
        打开浏览器
        :param browserName:浏览器名称
        '''
        try:
            if browserName.lower() == 'ie':
                self.driver = webdriver.Ie(executable_path= ieDriverFilePath)
            elif browserName.lower() == 'chrome':
                chrome_options = Options()
                chrome_options.add_experimental_option('excludeSwitches',['Chrome 正受到自动测试软件的控制'])
                self.driver = webdriver.Chrome(chrome_options=chrome_options)
                print('浏览器已经启动。。。')
            else:
                self.driver = webdriver.Firefox(executable_path= fireFoxDriverFilePath)
        except Exception as e:
            raise e


    def visit_url(self,url,*arg):
        '''
        访问url
        :param url:被访问的url
        '''
        try:
            self.driver.get(url)
        except Exception as e:
            raise e

    def close_browser(self,*arg):
        '''
        关闭浏览器
        '''
        try:
            self.driver.quit()
        except Exception as e:
            raise e


    def sleep(self,sleepSeconds,*arg):
        '''
        暂停
        :param sleepSeconds:暂停秒数
        '''
        try:
            time.sleep(int(sleepSeconds))
        except Exception as e:
            raise e


    def clear(self,locateType,locatorExpression):
        '''
        清除元素
        :param locateType:定位表达式
        :param locatorExpression:元素表达式
        '''
        try:
            # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
            # element.clear()
            getElement(self.driver,locateType,locatorExpression).clear()
        except Exception as e:
            raise e


    def input_string(self,locateType,locatorExpression,inputContent):
        '''
        输入内容
        :param locateType:定位表达式
        :param locatorExpression:元素表达式
        :param inputContent:输入内容
        '''
        try:
            # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
            # element.send_keys(inputContent)
            getElement(self.driver,locateType,locatorExpression).send_keys(inputContent)
        except Exception as e:
            raise e

    def click(self,locateType,locatorExpression,*arg):
        '''
        点击
        :param locateType:定位表达式
        :param locatorExpression:元素表达式
        '''
        try:
            # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
            # element.click()
            getElement(self.driver,locateType,locatorExpression).click()
        except Exception as e:
            raise e

    def capture_screen(self,*args):
        '''截图'''
        currTime = getCurrentTime()
        picNameAndPath = str(createCurrentDateDir()) + '\\' + str(currTime) + '.png'
        try:
            driver.get_screenshot_as_file(picNameAndPath.replace('\\', r'\\'))
        except Exception as e:
            raise e


    def assert_string_in_pageSource(self,assertString,*arg):
        '''验证页面元素
        :param:assertString:预期文字
        '''
        try:
            assert assertString in driver.page_source,'%s not found in page source!'%assertString
        except AssertionError as e:
            self.capture_screen(self.driver)
            raise AssertionError(e)
        except Exception as e:
            raise e


    def operate_window_handle(self):
        '''
        窗口跳转处理
        '''
        try:
            now_handle = self.driver.current_window_handle
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != now_handle:
                    self.driver.switch_to.window(handle)
        except Exception as e:
            raise e


    def maximize_browser(self):
        '''窗口最大化'''
        try:
            self.driver.maximize_window()
        except Exception as e:
            raise e

    def get_title(self):
        '''获取标题'''
        try:
            return self.driver.title
        except Exception as e:
            raise e

    def selectByValue(self,locateType,locatorExpression,value,*arg):
        '''
        通过value值选择
        :param locateType:定位表达式
        :param locatorExpression:元素表达式
        :param value:选择值
        '''
        try:
            # element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
            elementObj = getElement(self.driver,locateType,locatorExpression)
            Select(elementObj).select_by_value(value)
        except Exception as e:
            raise e

    def js(self,script):
        '''
        js
        :param script:脚本
        '''
        try:
            self.driver.execute_script(script)
        except Exception as e:
            raise e

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.baidu.com')
    searchBox = getElement(driver,'id','kw')
    print(searchBox.tag_name)
    aList = getElements(driver,'tag name', 'a')
    print(len(aList))
    driver.quit()
    