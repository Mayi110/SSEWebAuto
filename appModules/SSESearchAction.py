# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 14:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SSESearchAction.py
# @Software: PyCharm

from pageObjects.SSESearchPage import sseSearchPage
from time import sleep
from util.Log import *


class sseSearchAction(object):
    def __init__(self):
        print('sseSearch....')

    @staticmethod
    def sseSearchEnterAnnouncementPage(driver,companyCode,expectResult):
        logging.info('场景：公司代码查询，进入公司公告页面 测试开始。。。')
        try:
            SS = sseSearchPage(driver)

            logging.info('清除官网全站检索搜索框内容')
            SS.inputBoxObj().clear()
            logging.info('官网全站检索搜索框输入查询公司代码：%s'%companyCode)
            SS.inputBoxObj().send_keys(companyCode)
            logging.info('单击查询按钮')
            SS.searchButtonObj().click()
            logging.info('切换窗口')
            SS.switchWindowObj()
            sleep(8)
            logging.info('验证跳转页面元素:%s'%expectResult)
            SS.assertAnnouncementPageElementObj(expectResult)
        except Exception as e:
            raise e

    @staticmethod
    def sseSearchEnterWebSWDPage(driver,companyCode):
        logging.info('场景：公司代码查询，进入全站检索页面 测试开始。。。')
        try:
            SS = sseSearchPage(driver)

            logging.info('清除官网全站检索搜索框内容')
            SS.inputBoxObj().clear()
            logging.info('官网全站检索搜索框输入查询公司代码：%s'%companyCode)
            SS.inputBoxObj().send_keys(companyCode)
            logging.info('点击关联公司链接')
            SS.linkObj().click()
            sleep(8)
            # logging.info('验证跳转页面元素')
            # SS.assertWebSWDPageElementObj()
        except Exception as e:
            raise e

