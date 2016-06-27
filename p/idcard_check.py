# coding=utf-8
'''
Created on 2016年6月24日

@author: qiu
'''
ys = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
wis = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]


def get_checkcode(idcard):
    s = sum([wis[k] * int(v) for k, v in enumerate(idcard)])
    y = s % 11
    code = ys[y]
    return code

if __name__ == "__main__":
    print get_checkcode("42082119870902001")
