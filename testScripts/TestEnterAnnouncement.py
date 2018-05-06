# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:44
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : TestEnterAnnouncement.py
# @Software: PyCharm

import time
from appModules.EnterAnnouncementAction import enterAnnouncementAction
from selenium import webdriver


class EnterAnnouncementPageTest():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://www.sse.com.cn')
        driver.implicitly_wait(30)

        enterAnnouncementAction.announcement_enter(driver)
        time.sleep(3)
        assert '最新上市公司公告全文' in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()

if __name__ == '__main__':
    EnterAnnouncementPageTest()
    print('进入最新上市公告页面成功！')
