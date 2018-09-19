# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 14:24
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_general.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_announcement.po_general import generalPage
from pageObjects.po_common.po_commonPage import commonPage
from util.Log import *
from util.ObjectMap import *


class generalAction(object):
    def __init__(self):
        print('search...')

    @staticmethod
    def searchGeneralByAllCondition(driver,keyWord,value):
        try:
            CP = commonPage(driver)

            logging.info('清空关键字输入框内容')
            CP.keyWordObj().clear()
            sleep(1)

            logging.info('输入关键字：%s'%keyWord)
            CP.keyWordObj().send_keys(keyWord)
            sleep(1)

            logging.info('选择的值是:%s'%value)
            CP.singleSelectObj(value)

            logging.info('单击查询按钮')
            CP.searchButtonObj().click()
            sleep(5)

            operate_window_handle()
            logging.info('当前窗口的标题是:%s'%get_title())

            GP = generalPage(driver)

            logging.info('点击 公告 链接')
            GP.announcementLinkObj().click()
            sleep(5)
        except Exception as e:
            raise e