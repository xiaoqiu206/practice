# coding=utf-8
'''
Created on 2016年8月24日

@author: qiu
'''
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
f = logging.handlers.TimedRotatingFileHandler('log')
f.setLevel(logging.NOTSET)
f.setFormatter(formatter)
f2 = logging.handlers.RotatingFileHandler('1.txt')
f2.setLevel(logging.NOTSET)
f2.setFormatter(formatter)
logger.addHandler(f)
logger.addHandler(console)
logger.addHandler(f2)


logger.debug('msg')
logger.info('msg')