# coding=utf-8
'''
Created on 2016年8月31日

@author: qiu
'''
import peewee
from peewee import *

database = MySQLDatabase(
    'test', host='mysql', password='420821198709020018', user='steve')


class BaseModel(Model):

    class Meta:
        database = database


class Stations(BaseModel):
    station_id = PrimaryKeyField()
    phase = IntegerField()
    station_num = IntegerField()
    station_name = TextField()
    english_name = TextField(null=True)
    image = TextField(null=True)
    line_id = IntegerField()
    is_transfer = IntegerField()
    sequence = IntegerField()

    class Meta:
        db_table = 'STATIONS'


database.connect()

for i in Stations.select():
    print i.station_name
