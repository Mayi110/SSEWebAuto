# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 12:41
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_announcement.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_listedinfo.po_announcement import announcementPage
from util.Log import *
from util.ObjectMap import *


class announcementAction(object):
    def __init__(self):
        print('search...')

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
    def searchAnnouncementByAllCondition(driver,companyCode,keyword,type,startDate,endDate,assertString):
        try:
            AP = announcementPage(driver)

            logging.info('输入公司代码或者简称：%s'%companyCode)
            AP.companyCodeObj().send_keys(companyCode)
            sleep(1)

            logging.info('输入关键字：%s'%keyword)
            AP.keyWordObj().send_keys(keyword)
            sleep(1)

            logging.info('选择的公告类型是：%s'%type)
            AP.announcementTypeObj(type)
            sleep(1)

            logging.info('选择开始日期：%s'%startDate)
            AP.announcementStartDateObj().send_keys(startDate)

            logging.info('选择结束日期：%s'%endDate)
            AP.announcementEndDateObj().send_keys(endDate)
            sleep(1)

            logging.info('单击查询按钮')
            AP.searchButtonObj().click()
            sleep(5)

            logging.info('单击第一条公告链接')
            AP.announcementLinkObj().click()
            sleep(8)

            logging.info('验证跳转页面元素:%s'%assertString)
            assert_string_in_pageSource(assertString)

            logging.info('关闭第一条公告')
            AP.announcementCloseObj().click()
            sleep(1)

            logging.info('退出浏览器')
            close_browser()

        except Exception as e:
            raise e


