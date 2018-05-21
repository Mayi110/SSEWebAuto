# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 14:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_search.py
# @Software: PyCharm

from pageObjects.po_search.po_search import sseSearchPage
from action.pageAction2 import *

class sseSearchAction(object):

    def __init__(self):
        print('sseSearch....')

    # @staticmethod
    # def sseSearchEnterWebSWDPage(driver,companyCode):
    #     try:
    #         SS = sseSearchPage(driver)
    #
    #         logging.info('清除官网全站检索搜索框内容')
    #         SS.inputBoxObj().clear()
    #         logging.info('官网全站检索搜索框输入查询公司代码：%s'%companyCode)
    #         SS.inputBoxObj().send_keys(companyCode)
    #         sleep(2)
    #         logging.info('单击查询按钮')
    #         SS.searchButtonObj().click()
    #         logging.info('切换窗口')
    #         operate_window_handle()
    #         sleep(8)
    #         logging.info('获取当前窗口的标题:%s'%get_title())
    #     except Exception as e:
    #         raise e

    # @staticmethod
    # def sseSearchEnterAnnouncementPage(driver,companyCode):
    #     try:
    #         SS = sseSearchPage(driver)
    #
    #         logging.info('清除官网全站检索搜索框内容')
    #         SS.inputBoxObj().clear()
    #         sleep(driver,2)
    #         logging.info('官网全站检索搜索框输入查询公司代码：%s'%companyCode)
    #         SS.inputBoxObj().send_keys(companyCode)
    #         sleep(driver,5)
    #         logging.info('点击关联公司链接')
    #         SS.companyCodeLinkObj().click()
    #         logging.info('切换窗口')
    #         operate_window_handle(driver)
    #         sleep(driver,8)
    #         logging.info('获取当前窗口的标题:%s'%get_title(driver))
    #     except Exception as e:
    #         raise e
    @staticmethod
    def sseSearchEnterAnnouncementPage(driver,companyCode):
        try:
            SS = sseSearchPage(driver)

            # logging.info('清除官网全站检索搜索框内容')
            SS.inputBoxObj().clear()
            time.sleep(2)
            # logging.info('官网全站检索搜索框输入查询公司代码：%s'%companyCode)
            SS.inputBoxObj().send_keys(companyCode)
            time.sleep(5)
            # logging.info('点击关联公司链接')
            SS.companyCodeLinkObj().click()
            # logging.info('切换窗口')
            basePage.operate_window_handle(driver)
            time.sleep(8)
            # logging.info('获取当前窗口的标题:%s'%get_title())
        except Exception as e:
            raise e
if __name__ == '__main__':
    from action.commonAction import *
    from selenium import webdriver
    launchBrowser('chrome','http://www.sse.com.cn')
    sseSearchAction.sseSearchEnterAnnouncementPage(webdriver,'浦发')
    assertPageElement('张江高科')
