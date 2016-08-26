# coding=utf-8
'''
Created on 2016年8月25日
闭包的研究
@author: qiu
'''


def counter(start=0):
    count = [start]

    def incr():
        count = count + [3]
        count[0] += 1
        return 6
    return incr


count = counter(5)
print count()
