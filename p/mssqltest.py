# coding=utf-8
'''
Created on 2016年6月30日

@author: qiu
'''
import pymssql

conn = pymssql.connect(server='192.168.248.73',
                       user='steve',
                       password='123456',
                       database='master'
                       )
cursor = conn.cursor()
cursor.execute("select * from MSreplication_options")
rows = cursor.fethall()
print rows
conn.close()
