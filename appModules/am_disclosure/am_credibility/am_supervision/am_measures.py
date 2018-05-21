# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 9:46
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_measures.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_credibility.po_supervision.po_measures import measuresPage
from util.Log import *
from util.ObjectMap import *
from action.pageAction import *


class measuresAction(object):
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
        logging.info('当前窗口的标题是:%s'%get_title())

    @staticmethod
    def searchMeasuresByAll(driver,companyCode,keyWord,select,startDate,endDate):
        try:
            MP = measuresPage(driver)

            logging.info('清除公司代码或简称输入框的内容')
            MP.inputBoxObj().clear()
            logging.info('输入公司代码：%s'%companyCode)
            MP.inputBoxObj().send_keys(companyCode)
            sleep(2)

            logging.info('清除涉及对象输入框的内容')
            MP.sjdxObj().clear()
            logging.info('输入关键字：%s'%keyWord)
            MP.sjdxObj().send_keys(keyWord)

            logging.info('选择监管类型是：%s'%select)
            MP.jglxObj(select)
            sleep(1)

            logging.info('选择开始时间：%s'%startDate)
            MP.startDateObj().send_keys(startDate)

            logging.info('选择结束时间：%s'%endDate)
            MP.endDateObj().send_keys(endDate)

            logging.info('点击查询按钮')
            MP.searchButtonObj().click()
            sleep(5)

            logging.info('点击公告链接')
            MP.pdfLinkObj().click()

            logging.info('切换窗口')
            operate_window_handle()
            sleep(8)
            logging.info('获取当前窗口的标题:%s'%get_title())

            logging.info('退出浏览器')
            close_browser()
        except Exception as e:
            raise e
