# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 16:20
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : tc_bdae_promisho.py
# @Software: PyCharm

from appModules.am_disclosure.am_credibility.am_supervision.am_promisho import promishoAction
from util.Log import *
from action.commonAction import *

def test_searchPromishoByAllCondition():
    try:
        logging.info('场景：通过承诺履行全条件查询，进入详情页面 测试开始。。。')
        launchBrowser('chrome','http://www.sse.com.cn/disclosure/credibility/supervision/promisho/')
        promishoAction.searchPromishoByAll(webdriver,'603013','国家','1','1','2')
        promishoAction.assertPageElement('亚普股份')
    except Exception as e:
        raise e