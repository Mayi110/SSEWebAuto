# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 14:10
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : TestSearchAnnouncement.py
# @Software: PyCharm

import time
from appModules.EnterAnnouncementAction import enterAnnouncementAction
from appModules.SearchAnnouncementAction import searchAnnounceementAction
from selenium import webdriver
from util.Log import *


def LaunchBrowser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.sse.com.cn')
    driver.implicitly_wait(30)
    return driver

def test_searchAnnouncement():
    logging.info('公告查询测试开始。。。')
    try:
        driver = LaunchBrowser()
        logging.info('启动浏览器，访问上交所网站')
        enterAnnouncementAction.announcement_enter(driver)
        time.sleep(5)
        searchAnnounceementAction.searchAnnouncement(driver,'600000','浦发银行','2018-04-01','2018-05-07')
        time.sleep(3)
        assert '浦发银行' in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()


