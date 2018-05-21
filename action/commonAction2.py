# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 11:03
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : commonAction.py
# @Software: PyCharm

from action.pageAction import *

driver = None

def launchBrowser(driver,browserName,url):
    '''打开测试页面'''
    global driver
    # logging.info('打开浏览器：%s'%browserName)
    basePage.open_browser(driver,browserName)
    # logging.info('浏览器最大化')
    basePage.maximize_browser(driver)
    # logging.info('访问被测地址：%s'%url)
    basePage.visit_url(driver,url)
    basePage.sleep(driver,2)
    # logging.info('当前窗口的标题是:%s'%get_title())


def assertPageElement(driver,assertString):
    '''验证元素是否在页面上'''
    try:
        # logging.info('验证页面元素:%s'%assertString)
        basePage.assert_string_in_pageSource(driver,assertString)
        # logging.info('退出浏览器')
        basePage.close_browser(driver)
    except Exception as e:
        raise e
if __name__ == '__main__':
    from selenium import webdriver
    import time
    launchBrowser(webdriver,'chrome','http://www.baidu.com')
    time.sleep(2)
    assertPageElement(webdriver,'百度一下')
