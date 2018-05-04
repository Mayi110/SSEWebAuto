# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:01
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : AnnouncementAction.py
# @Software: PyCharm

import unittest
from time import sleep
from pageObjects.EnterAnnouncementPage import EnterAnnouncementPage

class AnnouncementAction(object):
    def __init__(self):
        print('announcement...')

    @staticmethod
    def announcement(driver):
        try:
            announcement = EnterAnnouncementPage(driver)
            announcement.disclosureObj().click()
            sleep(3)
            announcement.listedinfoObj().click()
            sleep(3)
            announcement.announcementObj().click()
        except Exception as e:
            raise e

if __name__ == '__main__':
    unittest.main()