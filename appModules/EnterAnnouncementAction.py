# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:01
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : EnterAnnouncementAction.py
# @Software: PyCharm

from time import sleep
from pageObjects.EnterAnnouncementPage import enterAnnouncementPage


class enterAnnouncementAction(object):
    def __init__(self):
        print('enter...')

    @staticmethod
    def announcement_enter(self):
        try:
            announcement = enterAnnouncementPage(self)
            announcement.disclosureObj().click()
            sleep(3)
            announcement.listedinfoObj().click()
            sleep(3)
            announcement.announcementObj().click()
        except Exception as e:
            raise e