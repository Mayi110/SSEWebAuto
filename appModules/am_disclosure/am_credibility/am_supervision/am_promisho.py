# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 16:04
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : am_promisho.py
# @Software: PyCharm

from pageObjects.po_disclosure.po_credibility.po_supervision.po_promisho import promishoPage
from util.Log import *
from util.ObjectMap import *
from action.pageAction import *


class promishoAction(object):
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
    def searchPromishoByAll(driver,companyCode,keyWord,promiseType,itemType,promiseStatus):
        try:
            PP = promishoPage(driver)

            logging.info('清除公司代码或简称输入框的内容')
            PP.inputBoxObj().clear()
            logging.info('输入公司代码：%s'%companyCode)
            PP.inputBoxObj().send_keys(companyCode)
            sleep(2)

            logging.info('清除涉及对象输入框的内容')
            PP.promiseMainNameObj().clear()
            logging.info('输入关键字：%s'%keyWord)
            PP.promiseMainNameObj().send_keys(keyWord)

            logging.info('选择承诺类型是：%s'%promiseType)
            PP.promiseTypeObj(promiseType)
            sleep(2)

            logging.info('选择承诺事项类别是：%s'%itemType)
            PP.itemTypeObj(itemType)
            sleep(2)

            logging.info('选择履行状态是：%s'%promiseStatus)
            PP.promiseStatusObj(promiseStatus)
            sleep(2)

            logging.info('点击查询按钮')
            PP.searchButtonObj().click()
            sleep(5)

            logging.info('点击公告链接')
            PP.linkObj().click()

            logging.info('切换窗口')
            operate_window_handle()
            sleep(8)
            logging.info('获取当前窗口的标题:%s'%get_title())
        except Exception as e:
            raise e

    @staticmethod
    def assertPageElement(assertString):
        try:
            logging.info('验证跳转页面元素:%s'%assertString)
            assert_string_in_pageSource(assertString)
            logging.info('退出浏览器')
            close_browser()
        except Exception as e:
            raise e