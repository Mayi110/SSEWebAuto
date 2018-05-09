# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:01
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : EnterAnnouncementAction.py
# @Software: PyCharm

from time import sleep
from pageObjects.EnterAnnouncementPage import enterAnnouncementPage
from util.Log import *


class enterAnnouncementAction(object):
    def __init__(self):
        print('enter...')

    @staticmethod
    def announcement_enter(self):
        logging.info('进入最新公告页面')
        try:
            announcement = enterAnnouncementPage(self)

            logging.info('点击 披露 链接')
            announcement.disclosureObj().click()
            sleep(3)

            logging.info('点击 上市公司信息 链接')
            announcement.listedinfoObj().click()
            sleep(3)

            logging.info('点击 最新公告 链接')
            announcement.announcementObj().click()
        except Exception as e:
            raise e