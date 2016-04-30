# coding=utf-8
'''
Created on 2016年4月23日
封装使用websocket的loghandler
@author: xiaoq
'''
from logging.handlers import HTTPHandler as H
import logging

logger = logging.getLogger(__name__)
http_handler = H(
    host="127.0.0.1:80", url='/')
logger.addHandler(http_handler)
logger.error("this is a error")
