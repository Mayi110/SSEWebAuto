# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:44
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : TestAnnouncementSearch.py
# @Software: PyCharm

from selenium import webdriver
import time
from appModules.AnnouncementAction import AnnouncementAction

class testEnterAnnouncementPage():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://www.sse.com.cn')
        driver.implicitly_wait(30)

        AnnouncementAction.announcement(driver)
        time.sleep(3)
        assert '最新上市公司公告全文'in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()

if __name__ == '__main__':
    testEnterAnnouncementPage()
    print('进入最新上市公告页面成功！')