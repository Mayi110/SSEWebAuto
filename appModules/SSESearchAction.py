# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 14:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SSESearchAction.py
# @Software: PyCharm

from pageObjects.SSESearchPage import sseSearchPage
from util.Log import *
from util.ObjectMap import *


class sseSearchAction(object):
    def __init__(self):
        print('sseSearch....')

    @staticmethod
    def LaunchBrowser(browserName,url):
        logging.info('打开浏览器：%s'%browserName)
        open_browser(browserName)
        logging.info('浏览器最大化')
        maximize_browser()
        logging.info('访问被测地址：%s'%url)
        visit_url(url)
        sleep(2)

    @staticmethod
    def sseSearchEnterWebSWDPage(driver,companyCode):
        try:
            SS = sseSearchPage(driver)

            logging.info('清除官网全站检索搜索框内容')
            SS.inputBoxObj().clear()
            logging.info('官网全站检索搜索框输入查询公司代码：%s'%companyCode)
            SS.inputBoxObj().send_keys(companyCode)
            sleep(2)
            logging.info('单击查询按钮')
            SS.searchButtonObj().click()
            logging.info('切换窗口')
            operate_window_handle()
            sleep(8)
            logging.info('获取当前窗口的标题:%s'%get_title())
        except Exception as e:
            raise e

    @staticmethod
    def sseSearchEnterAnnouncementPage(driver,companyCode):

        try:
            SS = sseSearchPage(driver)

            logging.info('清除官网全站检索搜索框内容')
            SS.inputBoxObj().clear()
            sleep(2)
            logging.info('官网全站检索搜索框输入查询公司代码：%s'%companyCode)
            SS.inputBoxObj().send_keys(companyCode)
            sleep(5)
            logging.info('点击关联公司链接')
            SS.companyCodeLinkObj().click()
            logging.info('切换窗口')
            operate_window_handle()
            sleep(8)
            logging.info('获取当前窗口的标题:%s'%get_title())
        except Exception as e:
            raise e

    @staticmethod
    def assertPageElement(assertString):
        try:
            logging.info('验证跳转页面元素:%s'%assertString)
            assert_string_in_pageSource(assertString)
            logging.info('退出')
            close_browser()
        except Exception as e:
            raise e