# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 11:03
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : commonAction.py
# @Software: PyCharm

from action.pageAction import *

driver = None

def launchBrowser(browserName,url):
    '''打开测试页面'''
    global driver
    try:
        # logging.info('打开浏览器：%s'%browserName)
        open_browser(browserName)
        # logging.info('浏览器最大化')
        maximize_browser()
        # logging.info('访问被测地址：%s'%url)
        visit_url(url)
        sleep(2)
        # logging.info('当前窗口的标题是:%s'%get_title())
    except Exception as e:
        raise e


def assertPageElement(assertString):
    '''验证元素是否在页面上'''
    try:
        # logging.info('验证页面元素:%s'%assertString)
        assert_string_in_pageSource(assertString)
        # logging.info('退出浏览器')
        close_browser()
    except Exception as e:
        raise e

if __name__ == '__main__':
    import time
    launchBrowser('chrome','http://www.baidu.com')
    time.sleep(2)
    assertPageElement('百度一下')
