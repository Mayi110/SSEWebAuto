# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 14:42
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : RunTest.py
# @Software: PyCharm

from HTMLTestRunner import HTMLTestRunner
import unittest
import time,os

report_path = os.path.join(os.getcwd(),'testReport')
case_path = os.path.join(os.getcwd(),'testCases')

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern='tc_search.py')
    return discover


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_abspath=os.path.join(report_path,now+' result.html')
    fp = open(report_abspath,'wb')
    runner = HTMLTestRunner(stream=fp,title='上交所官网自动化测试报告',description='环境：win7；浏览器：Chrome')
    runner.run(all_case())
    fp.close()
