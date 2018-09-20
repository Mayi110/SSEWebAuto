# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 15:20
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bcb_listing.py
# @Software: PyCharm

from action.commonAction import *
from appModules.am_disclosure.am_announcement.am_listing import listingAction
from util.Log import *
import unittest
import ddt

url = testUrl+'/disclosure/announcement/listing/'

@ddt.ddt
class listingCase(unittest.TestCase):
    '''上市/退市公告测试用例'''

    @ddt.data(['chrome','兵器工业','中国兵器工业集团有限公司'])
    @ddt.unpack
    def test_searchListingByAllCondition(self,browserName,keyWord,expectData):
        '''通过全部查询条件查询最新公告'''
        try:
            logging.info('场景：上市/退市公告业务 测试开始。。。')
            launchBrowser(browserName,url)
            listingAction.searchListingByAllCondition(webdriver,keyWord)
            assertPageElement(expectData)
        except Exception as e:
            raise e
    # test_searchAnnouncementByAllCondition()
if __name__ == '__main__':
    unittest.main()