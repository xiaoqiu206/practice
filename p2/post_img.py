# coding=utf-8
'''
Created on 2016年7月22日

@author: qiu
'''
import requests

url = 'http://hogan/chilineldser/doUserAction.php?act=addtask'

f = {'image': file('blackcat.jpg', 'rb')}
r = requests.session().post(url, files=f)
print r.status_code
print r.content
