# coding=utf-8
'''
Created on 2016年7月7日

@author: qiu
'''
import socket
import ssl
import json
import struct
import binascii
import time


def Payload(alert='', badge=1, data={}):
    payload = {
        'aps': {
            'alert': alert,
            'sound': 'k1DiveAlarm.caf',
            'badge': badge,
        },
        'acme': data,
    }
    return payload


def APN(tokens, payload, theCertfile):
    theHost = ('gateway.sandbox.push.apple.com', 2195)

    data = json.dumps(payload)

    # Clear out spaces in the device token and convert to hex
    notices = []
    for token in tokens:
        deviceToken = token.replace(' ', '')
        byteToken = binascii.unhexlify(deviceToken)

        theFormat = '!BH32sH%ds' % len(data)
        notice = struct.pack(theFormat, 0, 32, byteToken, len(data), data)
        notices.append(notice)

    # Create our connection using the certfile saved locally
    ssl_sock = ssl.wrap_socket(
        socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        certfile=theCertfile
    )
    ssl_sock.connect(theHost)

    # Write out our data
    for notice in notices:
        ssl_sock.write(notice)
    # Close the connection -- apple would prefer that we keep
    # a connection open and push data as needed.
    ''' 
    recv_data = struct.unpack('!BBI', recv_data)
    print recv_data
    '''
    ssl_sock.close()

    return True
