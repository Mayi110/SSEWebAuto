# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 9:48
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : TestSSESearch.py
# @Software: PyCharm

from selenium import webdriver
from appModules.SSESearchAction import sseSearchAction

def LaunchBrowser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.sse.com.cn')
    driver.implicitly_wait(30)
    return driver

def test_searchCompanyCodeEnterWebSearchPage():
    try:
        driver = LaunchBrowser()
        sseSearchAction.sseSearchEnterWebSWDPage(driver,'600015')
        # assert '上市公司公告全文' in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()

def test_searchCompanyCodeEnterAnnouncementPage():
    try:
        driver = LaunchBrowser()
        sseSearchAction.sseSearchEnterAnnouncementPage(driver,'600015','上市公司公告全文')
    except Exception as e:
        raise e
    finally:
        driver.quit()
