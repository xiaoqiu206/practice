# coding=utf-8
'''
Created on 2016年7月7日

@author: qiu
'''
from apnsclient import *

# 可以使用Session对象来维持连接池
session = Session()
con = session.get_connection("push_sandbox", cert_file="ck.pem")

# 发送推送和得到反馈
message = Message(["my", "device", "tokens"], alert="My message", badge=10)

# Send the message.
srv = APNs(con)
res = srv.send(message)

# Check failures. Check codes in APNs reference docs.
for token, reason in res.failed.items():
    code, errmsg = reason
    print "Device faled: {0}, reason: {1}".format(token, errmsg)

# Check failures not related to devices.
for code, errmsg in res.errors:
    print "Error: ", errmsg