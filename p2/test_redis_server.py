# coding=utf-8
'''
Created on 2016年8月23日

@author: qiu
'''
import redis

rc = redis.Redis(host='127.0.0.1', port=6379, db=0)
ps = rc.pubsub()
ps.subscribe(['count_alarm', 'iparlarm'])
for item in ps.listen():
    if item['type'] == 'message':
        print item['channel'], item['data']
