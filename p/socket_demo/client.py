# coding=utf-8
'''
Created on 2016年7月9日

@author: qiu
'''
import socket


def echo_data_run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8080))
    while 1:
        data = sock.recv(1024)
        if len(data) > 0:
            print data


if __name__ == "__main__":
    echo_data_run()
