# coding=utf-8
'''
Created on 2016年7月7日

@author: qiu
'''
import time
from apns import APNs, Frame, Payload


apns = APNs(use_sandbox=True, cert_file='public.pem',
            key_file='private.pem')

# Send a notification
token_hex = 'b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b87'
payload = Payload(alert="Hello World!", sound="default", badge=1)
apns.gateway_server.send_notification(token_hex, payload)

# Send multiple notifications in a single transmission
frame = Frame()
identifier = 1
expiry = time.time() + 3600
priority = 10
frame.add_item(token_hex, payload, identifier, expiry, priority)
apns.gateway_server.send_notification_multiple(frame)

# Get feedback messages
for (token_hex, fail_time) in apns.feedback_server.items():
    # do stuff with token_hex and fail_time
    print fail_time
