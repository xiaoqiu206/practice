# coding=utf-8
'''
Created on 2016年6月29日

@author: qiu
'''


def water(n):
    "2元一瓶水"
    start = n / 2
    gai = ping = 0
    x = 1
    while x <= start:
        # print "x:", x, "gai:", gai, "ping:", ping, "start:", start
        x += 1
        gai += 1
        ping += 1
        if gai == 4:
            gai = 0
            start += 1
        if ping == 2:
            ping = 0
            start += 1
    return start

print water(10)
