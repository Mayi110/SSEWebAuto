# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 12:41
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SearchAnnouncementAction.py
# @Software: PyCharm

from selenium import webdriver
import unittest
from pageObjects.SearchAnnouncementPage import searchAnnouncementPage


class searchAnnounceementAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchAnnouncement(driver,companyCode,keyword,type,startDate,endDate):
        try:
            SA = searchAnnouncementPage(driver)

            SA.companyCodeObj().clear()
            SA.companyCodeObj().send_keys(companyCode)

            SA.keyWordObj().clear()
            SA.keyWordObj().send_keys(keyword)

            SA.announcementTypeObj().select_by_value(type)

            SA.announcementStartDateObj().send_keys(startDate)
            SA.announcementEndDateObj().send_keys(endDate)

            SA.searchButtonObj().click()

            SA.announcementLinkObj().click()

            SA.announcementCloseObj().click()
        except Exception as e:
            raise e


if __name__ == '__main__':
    unittest.main()


