# coding=utf-8
'''
Created on 2016年7月8日

@author: qiu
'''
import socket
import ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(
    s, certfile='ck.pem')
ssl_sock.connect(('gateway.push.apple.com', 2195))
