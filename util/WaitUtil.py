# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 16:50
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : WaitUtil.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from action.PageAction import *


class WaitUtil(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,30)

