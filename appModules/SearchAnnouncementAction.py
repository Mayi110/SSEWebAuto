# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 12:41
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SearchAnnouncementAction.py
# @Software: PyCharm

from pageObjects.SearchAnnouncementPage import searchAnnouncementPage
from time import sleep
from util.Log import *


class searchAnnounceementAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchAnnouncement(driver,companyCode,keyword,startDate,endDate):
        logging.info('进入公告查询页面')
        try:
            SA = searchAnnouncementPage(driver)

            logging.info('输入公司代码或者简称')
            SA.companyCodeObj().send_keys(companyCode)
            sleep(1)

            logging.info('输入关键字')
            SA.keyWordObj().send_keys(keyword)
            sleep(1)

            logging.info('点击公告类型')
            SA.announcementTypeObj().click()
            sleep(1)

            logging.info('选择公告类型：定期公告')
            SA.announcementTypeOfDQGGObj().click()
            sleep(1)

            logging.info('选择开始日期')
            SA.announcementStartDateObj().send_keys(startDate)

            logging.info('选择结束日期')
            SA.announcementEndDateObj().send_keys(endDate)
            sleep(1)

            logging.info('单击查询按钮')
            SA.searchButtonObj().click()
            sleep(5)

            logging.info('单击第一条公告链接')
            SA.announcementLinkObj().click()
            sleep(8)

            logging.info('关闭第一条公告')
            SA.announcementCloseObj().click()
            sleep(1)
        except Exception as e:
            raise e


