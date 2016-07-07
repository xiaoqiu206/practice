# coding=utf-8
'''
Created on 2016年7月7日

@author: qiu
'''
from APNSWrapper import *
import binascii

# 请替换为自己的设备的deviceToken
deviceToken = binascii.unhexlify(
    "b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b87")

# 创建通知对象
notification = APNSNotification()
notification.token(deviceToken)
notification.alert("土豪，我们做朋友吧")
notification.badge(5)
notification.sound()

# 创建发送通知的这个wrapper
pem_cert_name = "ck.pem"  # 需要使用自己应用的P12证书
wrapper = APNSNotificationWrapper(
    pem_cert_name, True)  # 默认为连接正式环境，修改为True时连接沙盒环境
wrapper.append(notification)
wrapper.notify()
