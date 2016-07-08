# coding=utf-8
'''
Created on 2016年7月8日

@author: qiu
'''
import APNSWrapper
import binascii

deviceToken = binascii.unhexlify(
    '4d6417e58878ac9ec6d612a5ab0a7b85e567c77a6fbcbfc12a5f3d392aa9b0fc')

# create wrapper
wrapper = APNSWrapper.APNSNotificationWrapper('ck.pem', False)

# create message
message = APNSWrapper.APNSNotification()
message.token(deviceToken)
message.badge(5)
message.alert("hellowrold 234234")

# add message to tuple and send it to APNS server
wrapper.append(message)
wrapper.notify()
