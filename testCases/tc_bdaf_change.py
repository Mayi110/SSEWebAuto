# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 15:05
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bdaf_change.py
# @Software: PyCharm

from action.commonAction import *
from appModules.am_disclosure.am_credibility.am_supervision.am_change import changeAction
from util.Log import *
import unittest
from selenium import webdriver
from config.VarConfig import *
import ddt

url = testUrl+'/disclosure/credibility/supervision/change/'

@ddt.ddt
class changeCase(unittest.TestCase):
    '''董监高持股变动测试用例集合'''

    @ddt.data(['chrome','603160','杨奇志','2018-09-19','2018-09-21','深圳市汇顶科技股份有限公司'])
    @ddt.unpack
    def test_searchChangeByAllCondition(self,browserName,companyCode,userName,startDate,endDate,expectData):
        '''通过全条件查询一般公告信息'''
        try:
            logging.info('场景：通过董监高持股变动全条件查询，进入详情页面 测试开始。。。')
            launchBrowser(browserName,url)
            changeAction.searchChangeByAll(webdriver,companyCode,userName,startDate,endDate)
            assertPageElement(expectData)
        except Exception as e:
            raise e



if __name__ == '__main__':
    unittest.main()