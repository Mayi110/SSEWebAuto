# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 16:20
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ParseConfigurationFile.py
# @Software: PyCharm

from config.VarConfig import pageElementLocatorPath
from configparser import ConfigParser


class ParseConfigFile(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self,sectionName):
        optionsDic = dict(self.cf.items(sectionName))
        return optionsDic

    def getOptionValue(self,sectionName,optionName):
        value = self.cf.get(sectionName,optionName)
        return value