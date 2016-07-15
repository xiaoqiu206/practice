# coding=utf-8
'''
Created on 2016年7月9日

@author: qiu
'''
import socket
import time


def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8080)
    sock.bind(server_address)
    sock.listen(5)
    while 1:
        client, address = sock.accept()
        if client:
            while 1:
                client.send('123321')
                time.sleep(2)


def main():
    run_server()

if __name__ == "__main__":
    main()
