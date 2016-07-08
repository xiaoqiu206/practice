# coding=utf-8
'''
Created on 2016年7月7日

@author: qiu
'''
import native_apns
import time


def push(msg):
    # 推送需要用到的证书
    pem = 'new.pem'
    tokens = msg['tokens']
    data = msg['data']

    payload = native_apns.Payload(msg['content'], msg['count'], data)
    return native_apns.APN(tokens, payload, pem)

if __name__ == '__main__':
    msg = {
        'data': {'type': 'feed', 'id': 123},
        'count': 1,
        'tokens':  [
            'e1c04c5c5a02ff26e23251c1acfe6d38e8d4d3f5ba2dc68d2a932d50d20d791a',
            'ead30cb88a39b2f9e612212c1ecf34f415e826fb8192a61581d4a282bca77a0b',
        ],
        'content': 'ios推送测试20'
    }
    t1 = time.time()
    print push(msg)
    t2 = time.time()
    print 'cost time: %s s' % (t2 - t1)
