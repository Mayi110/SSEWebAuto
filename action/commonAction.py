# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 11:03
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : commonAction.py
# @Software: PyCharm



from util.Log import *
from action.pageAction import *

def launchBrowser(browserName,url):
    '''打开测试页面'''
    logging.info('打开浏览器：%s'%browserName)
    open_browser(browserName)
    logging.info('浏览器最大化')
    maximize_browser()
    logging.info('访问被测地址：%s'%url)
    visit_url(url)
    sleep(2)
    logging.info('当前窗口的标题是:%s'%get_title())

def assertPageElement(assertString):
    '''验证元素是否在页面上'''
    try:
        logging.info('验证页面元素:%s'%assertString)
        assert_string_in_pageSource(assertString)
        logging.info('退出浏览器')
        close_browser()
    except Exception as e:
        raise e