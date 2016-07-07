# coding=utf-8
'''
Created on 2016年7月7日

@author: qiu
'''
import sys
import native_apns


def push(msg):
    # 推送需要用到的证书
    pem = 'ck.pem'
    token = msg['udid']
    data = msg['data']

    payload = native_apns.Payload(msg['content'], msg['count'], data)
    return native_apns.APN(token, payload, pem)

if __name__ == '__main__':
    msg = {
        'data': {'type': 'feed', 'id': 123},
        'count': 8,
        'udid': 'b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b87',
        'content': 'ios推送测试'
    }
    print push(msg)
