# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 12:41
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SearchAnnouncementAction.py
# @Software: PyCharm

from selenium import webdriver
import unittest
from pageObjects.SearchAnnouncementPage import searchAnnouncementPage
from time import sleep


class searchAnnounceementAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchAnnouncement(driver,companyCode,keyword,value,startDate,endDate):
        try:
            SA = searchAnnouncementPage(driver)

            SA.companyCodeObj().send_keys(companyCode)
            sleep(2)

            SA.keyWordObj().send_keys(keyword)
            sleep(2)

            SA.announcementTypeObj(value=value)
            sleep(2)

            SA.announcementStartDateObj().send_keys(startDate)
            SA.announcementEndDateObj().send_keys(endDate)
            sleep(2)

            SA.searchButtonObj().click()
            sleep(5)

            SA.announcementLinkObj().click()
            sleep(2)

            SA.announcementCloseObj().click()
            sleep(2)
        except Exception as e:
            raise e


if __name__ == '__main__':
    unittest.main()


