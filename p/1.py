# coding=utf-8
'''
Created on 2016年5月4日
统计代码行数
@author: qiu
'''
import os

files = os.walk("/home/qiu/workspace/whhm/")
count1 = count2 = 0
for root, dir, files in files:
    if not dir:
        for each in files:
            if each.endswith('.py'):
                f = os.path.join(root, each)
                flines = len(file(f).readlines())
                count1 += flines
print count1


# 统计template里的html代码
files = os.walk("/home/qiu/workspace/whhm/templates")
for root, dir, files in files:
    if not dir:
        for each in files:
            f = os.path.join(root, each)
            flines = len(file(f).readlines())
            count2 += flines
print count2
print count1 + count2
