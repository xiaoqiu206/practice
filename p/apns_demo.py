# coding=utf-8
'''
Created on 2016年7月8日

@author: qiu
'''
import time
from apns import APNs, Frame, Payload

apns = APNs(use_sandbox=True, cert_file='new.pem')

# Send a notification
token_hex1 = 'e1c04c5c5a02ff26e23251c1acfe6d38e8d4d3f5ba2dc68d2a932d50d20d791a'
token_hex2 = 'ead30cb88a39b2f9e612212c1ecf34f415e826fb8192a61581d4a282bca77a0b'
token_hex3 = '0c7cd6cd7a2d328083d687440f12598656ff75e6e0a5ccbb3c369f30008d0955'
payload = Payload(alert="Hello World!", sound="default", badge=1)
frame = Frame()
identifier = 1
expiry = time.time() + 3600
priority = 10
frame.add_item(token_hex1, payload, identifier, expiry, priority)
frame.add_item(token_hex2, payload, identifier, expiry, priority)
frame.add_item(token_hex3, payload, identifier, expiry, priority)
# New APNS connection
feedback_connection = APNs(
    use_sandbox=True, key_file='private.pem', cert_file='public.pem')

# Get feedback messages.
for (token_hex, fail_time) in feedback_connection.feedback_server.items():
    # do stuff with token_hex and fail_time
    print token_hex, fail_time
