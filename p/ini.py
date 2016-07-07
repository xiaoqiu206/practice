# coding=utf-8
'''
Created on 2016年6月30日
解析ini文件
@author: qiu
'''
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('test.ini')
print config.sections()
print dict(config.items('t1'))